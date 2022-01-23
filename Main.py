import tkinter
from tkinter import messagebox
from tkinter import ttk
import random

window = tkinter.Tk()
window.title("TEST GAME")
window.geometry("800x600+800+300")
window.resizable(False, False)

# 프레임 생성. 버튼마다 새로운 프레임을 만들어 줌.
frame_top = tkinter.Frame(window, relief="raised", bd=2, width=800, height=50)
frame_bottom = tkinter.Frame(window, relief="flat", bd=2, width=800, height=150)
frame_secretary = tkinter.Frame(window, relief="raised", bd=2, width=550, height=400)
frame_hr = tkinter.Frame(window, relief="raised", bd=2, width=550, height=400)
frame_finance = tkinter.Frame(window, relief="raised", bd=2, width=550, height=400)
frame_business = tkinter.Frame(window, relief="raised", bd=2, width=550, height=400)
frame_rd = tkinter.Frame(window, relief="raised", bd=2, width=550, height=400)
frame_main = tkinter.Frame(window, relief="raised", bd=2, width=550, height=400)
frame_right = tkinter.Frame(window, relief="raised", bd=2, width=250, height=400)

# 프레임 배치.
frame_top.grid(row=0, column=0)
frame_bottom.grid(row=2, column=0)
frame_secretary.grid(row=1, column=0, sticky="w")
frame_hr.grid(row=1, column=0, sticky="w")
frame_finance.grid(row=1, column=0, sticky="w")
frame_business.grid(row=1, column=0, sticky="w")
frame_rd.grid(row=1, column=0, sticky="w")
frame_main.grid(row=1, column=0, sticky="w")
frame_right.grid(row=1, column=0, sticky="e")

# 프레임 변형 방지. 안하면 위젯크기에 맞춰서 자동 변형됨.
frame_top.grid_propagate(False)
frame_bottom.grid_propagate(False)
frame_secretary.grid_propagate(False)
frame_hr.grid_propagate(False)
frame_finance.grid_propagate(False)
frame_business.grid_propagate(False)
frame_rd.grid_propagate(False)
frame_main.grid_propagate(False)
frame_right.grid_propagate(False)

date = 1
year = 0
month = 1

timer_list = []

division_num = 0
division_list = []

work_list = []

task = {"인사": "hr", "경영지원": "management_support", "기획": "design", "재무": "finance"}

mail_num = 0  # 메일 개수
mail_storage = []  # 메일 저장공간

nation_list = ["korea", "china", "japan", "usa"]
goods_list = ["toothpaste", "wireless_battery", "lotion"]


def progress():  # 진행버튼 함수.
    date_manager()
    for i in timer_list:
        if date >= i["init_time"] + i["waiting_time"]:
            i["work"](i["person"], i["title"])
            timer_list.remove(i)


def esc_check_msg():  # 종료버튼 함수.
    is_quit = tkinter.messagebox.askyesno(title="알림", message="종료하시겠습니까?")
    if not is_quit:
        return
    window.destroy()


def frame_changer(frame):  # 프레임 전환 함수.
    frame.tkraise()


def date_manager():  # 진행버튼 누를때마다 날짜 올려주는 함수.
    global date, year, month
    month += 1
    if month >= 12:
        year += 1
        month = 1
    date_label.config(text="%d년 %d월" % (year, month))
    date = (year*12) + month


# 제거되어야할 위젯 리스트. alert label을 제외한 다른 위젯은 실행될 때 이 리스트에 추가되고 메인버튼 등을 누를 때 삭제된다.
widgets_willbe_destroyed = []


def alert_manager(about):  # 오른쪽 프레임에서 알림 출력하는 함수. about 인수에 버튼명 기입하면 관련 알림 출력.
    if about == main_btn:
        for i in widgets_willbe_destroyed:
            i.destroy()
        alert_label.config(text="메인화면으로 돌아갑니다.")
    elif about == finance_btn:
        alert_label.config(text="재무 버튼입니다.")
    elif about == "기획계획서":
        alert_label.config(text="안녕하십니까?\n\n이번 회장님이 지시하신 기획계획서\n보내드립니다.\n\n"
                                "추진할 사업을 선택해 주시면\n감사드리겠습니다.")


# 인사 파트
def add_division():
    alert_label.config(text="부서를 추가합니다.\n\n부서정보를 입력하세요.")

    add_label = tkinter.Label(frame_right, text="부서이름: ")
    add_label.place(x=10, y=150)
    widgets_willbe_destroyed.append(add_label)

    name_entry = ttk.Entry(frame_right, width=20)
    name_entry.place(x=75, y=150)
    widgets_willbe_destroyed.append(name_entry)

    assignment_label = tkinter.Label(frame_right, text="담당업무: ")
    assignment_label.place(x=10, y=180)
    widgets_willbe_destroyed.append(assignment_label)

    work_assignment = ttk.Combobox(frame_right, width=20, values=["인사", "경영지원", "기획", "재무"])
    work_assignment.place(x=75, y=180)
    widgets_willbe_destroyed.append(work_assignment)

    def confirm():
        global division_num
        division_list.append({"이름": name_entry.get(), "직원수": 0, "업무": task[work_assignment.get()],
                              "업무처리량": 0, "역량": 0, "능률": 0})
        division_num += 1
        division_tree_shower(True)

    confirm_btn = tkinter.Button(frame_right, text="확  인", command=confirm)
    confirm_btn.place(x=75, y=300)
    widgets_willbe_destroyed.append(confirm_btn)


def division_tree_shower(update):
    repeat_num = 1
    while repeat_num >= 1:
        division_tree = ttk.Treeview(frame_hr, column=("c1", "c2", "c3", "c4", "c5"), show="headings", height=10)
        division_tree.column("#1", anchor="w", width=120)
        division_tree.heading("#1", text="부 서 명")
        division_tree.column("#2", anchor="w", width=75)
        division_tree.heading("#2", text="직 원 수")
        division_tree.column("#3", anchor="center", width=160)
        division_tree.heading("#3", text="할당업무")
        division_tree.column("#4", anchor="center", width=75)
        division_tree.heading("#4", text="역    량")
        division_tree.column("#5", anchor="center", width=75)
        division_tree.heading("#5", text="능    률")

        # 부서 목록 스크롤바 생성
        division_scroll_bar = tkinter.Scrollbar(frame_hr)
        division_scroll_bar.grid(row=0, column=1, sticky="ns")

        # 부서 목록 트리뷰와 스크롤바 매칭, 배치
        division_tree.config(yscrollcommand=division_scroll_bar.set)
        division_tree.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        division_add_btn = tkinter.Button(frame_hr, text="부서 추가", command=add_division)
        division_add_btn.grid(row=1, column=0)

        for i in range(division_num):  # 부서 수만큼 저장한 것 불러오기
            division_tree.insert("", "end", text=division_list[i]["이름"],
                                 values=(division_list[i]["이름"], division_list[i]["직원수"],
                                         division_list[i]["업무"], division_list[i]["역량"],
                                         division_list[i]["능률"]))

        repeat_num = 0

        if update:
            division_tree.destroy()
            division_scroll_bar.destroy()
            division_add_btn.destroy()
            repeat_num = 1
            update = False


# 메일 파트
def create_mail_popup():
    global mail_num
    mail_popup = tkinter.Toplevel(frame_secretary)
    mail_popup.title("메  일")
    mail_popup.geometry("600x300+700+400")
    mail_popup.resizable(False, False)

    # 메일 열: 제목, 날짜, 발신인, 확인여부
    mail_tree = ttk.Treeview(mail_popup, column=("c1", "c2", "c3", "c4"), show="headings", height=10)
    mail_tree.column("#1", anchor="w", width=110)
    mail_tree.heading("#1", text="발 신 인")
    mail_tree.column("#2", anchor="w", width=270)
    mail_tree.heading("#2", text="제    목")
    mail_tree.column("#3", anchor="center", width=110)
    mail_tree.heading("#3", text="날    짜")
    mail_tree.column("#4", anchor="center", width=80)
    mail_tree.heading("#4", text="확인여부")

    # 메일 스크롤바 생성
    mail_scroll_bar = tkinter.Scrollbar(mail_popup)
    mail_scroll_bar.grid(row=0, column=1, sticky="ns")

    # 메일 트리뷰와 스크롤바 매칭, 배치
    mail_tree.config(yscrollcommand=mail_scroll_bar.set)
    mail_tree.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

    for i in range(mail_num):  # 메일 개수만큼 저장한 것 불러오기
        mail_tree.insert("", 0, text=mail_storage[i]["title"],
                         values=(mail_storage[i]["person"], mail_storage[i]["title"],
                                 "{0}년 {1}월".format(mail_storage[i]["date_y"], mail_storage[i]["date_m"]),
                                 mail_storage[i]["is_checked"]))

    def read():
        title = mail_tree.item(mail_tree.focus(), "values")[1]
        if title == "기획계획서":
            design_plan()
        mail_popup.destroy()

    read_btn = tkinter.Button(mail_popup, command=read, text="읽  기", width=10, height=2)
    read_btn.grid(row=1, column=0, pady=(10, 0))


# 메일 전송 함수. 메일 저장공간에 저장하고, 메일 개수 1 추가
def mail_sending(person, title):
    global mail_num
    mail_storage.append({"person": person, "title": title, "date_y": year, "date_m": month,
                          "is_checked": "N"})
    mail_num += 1


# 기획파트
def design_plan():
    value_list = []

    def design_info_show(event):
        for i in work_list:
            if i["제목"] == design_plans_box.get():
                design_info.config(text="상품목: {0}\n\n구입처: {1}\n\n판매처: {2}\n\n"
                                   .format(i["상품"], i["구매지"], i["판매지"]))

    for i in work_list:
        value_list.append(i["제목"])

    alert_manager("기획계획서")
    design_plans_box = ttk.Combobox(frame_right, values=tuple([]))
    design_plans_box["values"] = tuple(value_list)
    design_plans_box.place(x=10, y=100)

    design_info = tkinter.Label(frame_right, text="")
    design_info.place(x=10, y=200)

    widgets_willbe_destroyed.append(design_plans_box)
    widgets_willbe_destroyed.append(design_info)

    design_plans_box.bind("<<ComboboxSelected>>", design_info_show)

    financial_esti_btn = tkinter.Button(frame_right, text="사업성 평가",
                                        command=financial_estimate)
    financial_esti_btn.place(x=75, y=300)



def design_execute():
    alert_label.config(text="수출, 수입할 상품을 기획합니다.\n\n담당 부서를 선택하여 업무를 할당하세요.")
    value_list = []

    for i in division_list:
        value_list.append(i["이름"])

    def printIt(event):
        print(division_assignment.get())

    division_assignment = ttk.Combobox(frame_right, values=tuple([]))
    division_assignment['values'] = tuple(value_list)
    division_assignment.place(x=10, y=100)
    division_assignment.bind("<<ComboboxSelected>>", printIt)

    widgets_willbe_destroyed.append(division_assignment)

    def title_maker(buy_p, sell_p, goods):
        if buy_p == "korea":
            return str(goods) + " " + str(sell_p) + " 수출 " + "사업"
        elif buy_p != "korea":
            return str(sell_p) + " " + str(goods) + " 수입 " + "사업"

    def confirm(title, buy_p, sell_p, goods, date):
        confirm_box = tkinter.messagebox.askyesno(title="확인", message="기획을 추진하시겠습니까?")
        if confirm_box:
            work_list.append({"제목": title, "구매지": buy_p, "판매지": sell_p,
                              "상품": goods, "날짜": date})

            timer_list.append({"init_time": date, "waiting_time": 3,
                               "work": mail_sending, "person": "홍길동", "title": "기획계획서"})

    confirm_btn = tkinter.Button(frame_right,
                                 command=lambda:confirm("테스트", "korea", "japan", "toothpaste", date),
                                 text="확  인", width=10, height=2)
    confirm_btn.place(x=75, y=150)

    widgets_willbe_destroyed.append(confirm_btn)




# 재무 파트
def financial_estimate():
    do_it = tkinter.messagebox.askyesno(title="사업성 평가", message="진행하시겠습니까?")
    if not do_it:
        return
    for i in widgets_willbe_destroyed:
        i.destroy()
    frame_changer(frame_main)





# 날짜 라벨.
date_label = tkinter.Label(frame_top, text="%d년 %d월" % (year, month))
date_label.place(x=390, y=12)

# 오른쪽 프레임 알림 라벨.
alert_label = tkinter.Label(frame_right, text="", justify="left")
alert_label.place(x=10, y=10)

# 종료 버튼.
esc_btn = tkinter.Button(frame_top, text="종  료", command=esc_check_msg, width=10, height=2)
esc_btn.place(x=715, y=2.5)


# 메인메뉴 버튼 생성.
main_btn = tkinter.Button(frame_top, text="메인메뉴", width=10, height=2,
                          command=lambda: [frame_changer(frame_main), alert_manager(main_btn)])
main_btn.place(x=2.5, y=2.5)

secretary_btn = tkinter.Button(frame_main, text="비   서   실", bg="gray99", font=15, width=45, height=3,
                               command=lambda: frame_changer(frame_secretary))
hr_btn = tkinter.Button(frame_main, text="인    사", bg="gray99", font=15, width=20, height=3,
                        command=lambda: [frame_changer(frame_hr), division_tree_shower(False)])
finance_btn = tkinter.Button(frame_main, text="재    무", bg="gray99", font=15, width=20, height=3,
                             command=lambda: [frame_changer(frame_finance), alert_manager(finance_btn)])
business_btn = tkinter.Button(frame_main, text="영    업", bg="gray99", font=15, width=20, height=3,
                              command=lambda: frame_changer(frame_business))
rd_btn = tkinter.Button(frame_main, text="연구개발", bg="gray99", font=15, width=20, height=3,
                        command=lambda: frame_changer(frame_rd))
progress_btn = tkinter.Button(frame_main, text="진        행", bg="gray99", font=15, width=45, height=3,
                              command=progress)


# 메인메뉴 버튼 배치.
secretary_btn.place(x=65, y=30)
hr_btn.place(x=65, y=120)
finance_btn.place(x=290, y=120)
business_btn.place(x=65, y=210)
rd_btn.place(x=290, y=210)
progress_btn.place(x=65, y=300)


# 비서실 버튼 생성.
mail_btn = tkinter.Button(frame_secretary, command=create_mail_popup, text="메  일", width=10, height=2)
mail_btn.place(x=460, y=2.5)


# 기획 버튼 생성
design_btn = tkinter.Button(frame_business, command=design_execute, text="기  획", width=10, height=2)
design_btn.place(x=460, y=2.5)


class BusinessItem:
    def __init__(self):
        self.name = ""
        self.performance = 0
        self.price = 0
        self.popularity = 0
        self.competition = 0


class Timer:
    def __init__(self):
        self.init_time = 0
        self.waiting_time = 0
        self.work = ""











'''
def back(frame):
    frame.tkraise()

backBtn = tkinter.Button(frame_left, text="뒤로가기", command=lambda: back(frame_left2))
backBtn.pack()

label1 = tkinter.Label(frame_left, text="Hello, World!")
label2 = tkinter.Label(frame_right, text="Welcome to tkinter!")
label1.pack()
label2.pack()
'''

window.mainloop()
