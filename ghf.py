csdl_goc=[["Câu 1: Trí tuệ nhân tạo (AI)\nlà gì?", "A. Một loại phần mềm", "B. Một loại phần cứng", "C. Khả năng máy tính học và\nsuy nghĩ như con người", "D. Một hệ điều hành", 2, 0], ["Câu 2: AI có thể ứng dụng\ntrong lĩnh vực nào sau đây?", "A. Y tế", "B. Giáo dục", "C. Giao thông", "D. Tất cả các lĩnh vực trên", 3, 0], ["Câu 3: Một ví dụ về ứng dụng\ncủa AI là gì?", "A. Phần mềm xử lý văn bản", "B. Hệ thống tự động lái xe", "C. Máy in", "D. Máy quét mã vạch", 4, 0], ["Câu 4: AI có thể thực hiện\ncác nhiệm vụ nào sau đây?", "A. Nhận diện giọng nói", "B. Dịch ngôn ngữ", "C. Chơi cờ vua", "D. Tất cả các nhiệm vụ trên", 4, 0]]
#Khi tạo chương trình 1 biến tên csdl_goc lưu trữ dữ liệu của câu gỏi sẽ ở vị trí này


#Khai báo các thư viện
from tkinter import *
import random
import time
from tkinter.ttk import Combobox
from tkinter import  messagebox
import copy
import threading


class RoundedButton(Canvas):#đối tượng này là nút có góc tròn, dùng để chứa các câu trả lời

    def __init__(self, master=None, text:str="", radius=25, btnforeground="#000000", btnbackground="#ffffff", clicked=None, *args, **kwargs):
        super(RoundedButton, self).__init__(master, *args, **kwargs)
        self.config(bg=self.master["bg"])
        self.btnbackground = btnbackground
        self.clicked = clicked

        self.radius = radius  
   
        self.rect = self.round_rectangle(0, 0, 0, 0, tags="button", radius=radius, fill=btnbackground)
        self.text = self.create_text(0, 0, text=text, tags="button", fill=btnforeground, font=("Times", 9), justify="center")

        self.tag_bind("button", "<ButtonPress>", self.border)
        self.tag_bind("button", "<ButtonRelease>", self.border)
        self.bind("<Configure>", self.resize)
   
        text_rect = self.bbox(self.text)
        if int(self["width"]) < text_rect[2]-text_rect[0]:
            self["width"] = (text_rect[2]-text_rect[0]) + 10
   
        if int(self["height"]) < text_rect[3]-text_rect[1]:
            self["height"] = (text_rect[3]-text_rect[1]) + 10
    def doimau(self,mau_nen,mau_chu):
        self.btnbackground = mau_nen
        self.btnforeground = mau_chu
        self.itemconfig(self.rect, fill=self.btnbackground)
        self.itemconfig(self.text, fill=self.btnforeground)
    def round_rectangle(self, x1, y1, x2, y2, radius=25, update=False, **kwargs): # if update is False a new rounded rectangle's id will be returned else updates existing rounded rect.
        # source: https://stackoverflow.com/a/44100075/15993687
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]

        if not update:
            return self.create_polygon(points, **kwargs, smooth=True)
   
        else:
            self.coords(self.rect, points)

    def resize(self, event):
        text_bbox = self.bbox(self.text)

        if self.radius > event.width or self.radius > event.height:
            radius = min((event.width, event.height))

        else:
            radius = self.radius

        width, height = event.width, event.height

        if event.width < text_bbox[2]-text_bbox[0]:
            width = text_bbox[2]-text_bbox[0] + 30
   
        if event.height < text_bbox[3]-text_bbox[1]:
            height = text_bbox[3]-text_bbox[1] + 30
   
        self.round_rectangle(5, 5, width-5, height-5, radius, update=True)

        bbox = self.bbox(self.rect)

        x = ((bbox[2]-bbox[0])/2) - ((text_bbox[2]-text_bbox[0])/2)
        y = ((bbox[3]-bbox[1])/2) - ((text_bbox[3]-text_bbox[1])/2)

        self.moveto(self.text, x, y)

    def border(self, event):
        if event.type == "4":
            if self.clicked is not None:
                self.clicked()

        else:
            self.itemconfig(self.rect, fill=self.btnbackground)
    def set_button_color(self, color):
        self.itemconfig(self.rect, fill=color)
def tat_chuong_trinh():#hàm tắt chương trình
    root.destroy()
def doi_mau(nut,mau):#hàm để đổi màu 1 nút
    nut.config(bg=mau)
def vo_hieu_4_nut():#làm mất trạng thái hoạt động,mất màu của 4 câu trả lời
    a.config(state=DISABLED)
    b.config(state=DISABLED)
    c.config(state=DISABLED)
    d.config(state=DISABLED)
    a.doimau("gray","white")
    b.doimau("gray","white")
    c.doimau("gray","white")
    d.doimau("gray","white")



def switch():#hàm này làm đổi văn bản trong nút có liên kết với hàm này từ "ON" sang "OFF" và ngược lại
    global is_on,on_button

    if is_on:
        on_button.config(text="OFF")

        is_on = False
    else:
 
        on_button.config(text="ON")

        is_on = True

def tg_c_cauhoi(box_tg,tg_lam_bai):
    global tg_chuyen_cau_hoi,thoigiandelambai,sl_ch,biencamco
    tg_chuyen_cau_hoi=box_tg.get()


    sl_ch=int(so_luong_cau_hoi.get())
    if thoigiandelambai!="Không giới hạn":
        biencamco=True
        thoigiandelambai=int(thoigiandelambai)*60+1
    else:
        biencamco=False

def ktinput(n,tg_lam_bai,tgchuyencauhoi):
    #Khi ấn nút "BẮT ĐẦU" hàm này hoạt động để kiểm tra các đầu vào có thỏa mãn điều kiện không,
    #Nếu có thì bắt đầu làm trắc nghiệm ngược lại thì không có gì xảy ra
    global csdl_goc,box_tg,thoigiandelambai,tg_chuyen_cau_hoi,SO_LUONG_CAU_TRA_LOI_DUNG,csdl_goc,csdl,sl_ch
    csdl=copy.copy(csdl_goc)
    tg_chuyen_cau_hoi=int(tgchuyencauhoi)
    if( not n.isdigit()):return
    if int(n)>len(csdl_goc) or int(n)<=0:
        return
    sl_ch=n
    thoigiandelambai=tg_lam_bai.get()
 
    tg_c_cauhoi(box_tg,tg_lam_bai)
    SO_LUONG_CAU_TRA_LOI_DUNG=0
    main()
def xem_lai():#hàm này xóa hết mọi thứ trên màn hình rồi Gọi hàm main() để xem lại bài hàm
    global nut2,sl_ch,thoigiandelambai,caudung
    global stt,screen_width,screen_height,csdl,csdl_goc
    global cau_hoi,a,b,c,d,bo_qua,biencamco,lui,dau,cua_so,nut_lam_lai,nut_thoat,nut_xem_lai,diemso,hienthimeme,image_label
    global tg_chuyen_cau_hoi,dulieu,stt_cauhoi
    stt=0
    cua_so.destroy()
    nut_lam_lai.destroy()
    nut_thoat.destroy()
    nut_xem_lai.destroy()
    diemso.destroy()
    main(True)
def lam_lai(cua_so, nut_lam_lai, nut_thoat):#hàm này xóa mọi thứ trên màn hình và gọi hàm menu để làm lại bài trắc nghiệm
    global csdl,sl_ch,thoigiandelambai,biencamco,on,off
    global stt,screen_width,screen_height
    global cau_hoi,a,b,c,d,canvas,csdl_goc,sl_ch
    global tg_chuyen_cau_hoi,on,off,is_on,on_button,SO_LUONG_CAU_TRA_LOI_DUNG
    for i in range (sl_ch):
        csdl_goc[i][6]=0
    stt=0
    cua_so.destroy()
    nut_lam_lai.destroy()
    nut_thoat.destroy()
    canvas.destroy()
    is_on=True
    csdl=copy.copy(csdl_goc)
    menu()
    root.mainloop()
def Nop_Bai(co_phai_xem_lai_khong=False):#hàm nộp bài (nếu đang trong chế độ xem lại thì hàm này  có nội dung là quay lại)

    global stt,a,b,c,d,cauhoi,cau_hoi,canvas,csdl,screen_width,screen_height,image,tg_chuyen_cau_hoi,bo_qua,is_on,button_exit,button_setting, button_next,thoigiandelambai,sl_ch,biencamco
    global dulieu,button_lui,button_dau,dau,lui,stt_cauhoi,SO_LUONG_CAU_TRA_LOI_DUNG
    global cua_so,nut_lam_lai,nut_thoat,nut_xem_lai,diemso,hienthimeme,image_label #các nút,label,ảnh
    if Kiem_tra_xem_da_lam_het_cac_cau_hoi_chua(co_phai_xem_lai_khong):
        thoigiandelambai=0
        canvas.destroy()
        a.destroy()
        b.destroy()
        c.destroy()
        d.destroy()
        if not co_phai_xem_lai_khong:
            for i in range(sl_ch):
                if csdl[i][5]==csdl[i][6] :
                    SO_LUONG_CAU_TRA_LOI_DUNG+=1
   

        left = screen_width/3.2
        top = screen_height*10/100
        right = screen_width-screen_width/3.2
        bottom = screen_width*55/100
        cua_so=Canvas(root,bg="white",height=screen_height,width=screen_width)
        cua_so.place(x=0,y=0)
        ti=round(SO_LUONG_CAU_TRA_LOI_DUNG/sl_ch,4)

        ti=ti*100
        ti=round(ti,2)



   
        diemso=Label(root,text=f"Trả lời đúng: {SO_LUONG_CAU_TRA_LOI_DUNG}/{sl_ch}\nTỉ lệ: {ti}%",bd=0,compound="center",font=("Arial",15),fg=("#7FFF00" if ti>=50 else "red"))
        diemso.place(x=screen_width*20//100,y=screen_height*50//100)


        #nút làm lại
        nut_lam_lai=Button(root,text="LÀM LẠI",bd=0,compound="center",font=("Arial",15),command= lambda : lam_lai(cua_so, nut_lam_lai, nut_thoat))
        nut_lam_lai.place(x=screen_width*20//100,y=screen_height*20/100)#vị trí nút làm lại
        #nút xem lại
        nut_xem_lai=Button(root,text="XEM LẠI",bd=0,compound="center",font=("Arial",15),command= lambda : xem_lai())
        nut_xem_lai.place(x=screen_width*20//100,y=screen_height*30/100)#vị trí nút làm lại
        #nút thoát
        nut_thoat=Button(root,text="THOÁT",bd=0,compound="center",font=("Arial",15),command=tat_chuong_trinh)
        nut_thoat.place(x=screen_width*20//100,y=screen_height*40/100)#vị trí nút thoát
        root.mainloop()


def start_delayed_task():#tạo ra 1 luồng riêng để có thể thao tác khi chương trình đang trong thời gian chờ để chuyển câu hỏi
    thread = threading.Thread(target=delayed_task)
    thread.start()
kt=False#biến này là 1 biến cầm cờ, nếu chương trình đang trong thời gian chờ để chuyển câu hỏi mà người dùng thao tác thì chương trình sẽ không thực hiện
# việc chuyển câu hỏi trước đó nữa
def delayed_task():
    global nut2,sl_ch,thoigiandelambai,caudung
    global stt,screen_width,screen_height,csdl,csdl_goc
    global cau_hoi,a,b,c,d,bo_qua,biencamco,lui,dau,thoat_khoi_chuyen_cau_hoi
    global tg_chuyen_cau_hoi,dulieu,stt_cauhoi,SO_LUONG_CAU_TRA_LOI_DUNG,kt



    if kt==True:
        return
    kt=True
    if int(tg_chuyen_cau_hoi)>0:#nếu có thời gian chuyển câu hỏi thì chương trình sẽ chờ trong khoảng thời gian đó
        for i in range(10000):
            time.sleep(int(tg_chuyen_cau_hoi)/10000)
        kt=False
    kt=False
    if stt!=sl_ch-1:#nếu câu hỏi hiện tại khác câu cuối cùng thì tự chuyển sang câu hỏi tiếp theo
        chuyen_cau_hoi(1)

def chuyen_sang_cau_hoi_tiep_theo(nut,cau_tra_loi,dap_an):#khi người dùng ấn chọn đáp án thì sử dụng hàm start_delayed_task() để tự chuyển câu hỏi
    global nut2,sl_ch,thoigiandelambai,caudung
    global stt,screen_width,screen_height,csdl,csdl_goc
    global cau_hoi,a,b,c,d,bo_qua,biencamco,lui,dau,thoat_khoi_chuyen_cau_hoi
    global tg_chuyen_cau_hoi,dulieu,stt_cauhoi,SO_LUONG_CAU_TRA_LOI_DUNG,kt
    if stt<sl_ch:
        csdl[stt][6]=cau_tra_loi
    a.doimau("white","black")
    b.doimau("white","black")
    c.doimau("white","black")
    d.doimau("white","black")
    nut.doimau("yellow","black")
    root.update()
    if stt==sl_ch-1:
        return
   
    start_delayed_task()






def xoa_cd(canvas2,box_tg):#phá cài đặt để tiếp tục làm bài
    global tg_chuyen_cau_hoi
    tg_chuyen_cau_hoi=int(box_tg.get())#cập nhật thời gian chuyển câu hỏi
 

    canvas2.destroy()
 
def tao_cd():#chuyển sang cài đặt
    global tg_chuyen_cau_hoi

    canvas2 = Canvas(canvas,width=screen_width,height=screen_height,bg="white")#tạo canvas
    canvas2.place(x=0,y=0)

    Label (canvas2,text="",font=("Times New Roman",22),bg="white",width=int(screen_width/18),height=int(screen_height/70)).place(x=int(screen_width/100),y=int(screen_height/50))
    Label(canvas2,text="Thời gian chuyển câu hỏi",font=("Arial",9),bg="white").place(x=screen_width*5/100,y=screen_height*5/100)

    #combobox để người dùng cập nhật thời gian chuyển câu hỏi
    #các lựa chọn của combobox
    tg=['0','1','2','3','4','5','6','7']
    # Khởi tạo combobox
    box_tg = Combobox(canvas2,font=("Arial",9),width=13,values=tg,state="readonly")
    box_tg.place(x=screen_width*30/100,y=screen_height*8/100)
   
    # Thiết lập giá trị mặc định cho combobox
    box_tg.set(tg_chuyen_cau_hoi)

    tg_chuyen_cau_hoi=box_tg.get()


  
    #nút quaylai này sẽ quá màn hình cài đặt đang hoạt động
    quaylai=Button(canvas2,text="<=",font=("Arial",9),command= lambda : xoa_cd(canvas2,box_tg),bg="#FF3478",activebackground="#FF3478", relief="flat", borderwidth=0)

    quaylai.place(x=screen_width*80//100,y=screen_height*10/100)


def show_failure_message():#người dung hết thời gian làm bài
    global stt
    #hỏi xem người dùng còn muốn làm bài không, nếu chọn "yes" thì không có gì xảy ra
    #nếu chọn "no" thì gọi hàm Nop_Bai để nộp bài
    answer = messagebox.askquestion("Tiếp tục?", "Bạn đã hết thời gian\n làm bài trắc nghiệm\nbạn muốn tiếp tục không?")
    if answer == 'no':
        Nop_Bai()
       
#Khi người dùng nộp bài hàm này sẽ hỏi lại xem họ có chắc là muốn nộp bài không và nhắc về những câu hỏi chưa làm 
def Kiem_tra_xem_da_lam_het_cac_cau_hoi_chua(co_phai_xem_lai_khong):
    global sl_ch,csdl
    if co_phai_xem_lai_khong: return True#nếu đang trong chế độ xem lại thì bỏ qua hàm này
    cac_cau_hoi_chua_lam=''
    for i in range(sl_ch):
        if csdl[i][6]==0:
            cac_cau_hoi_chua_lam+=str(i+1)+", "
    if not len(cac_cau_hoi_chua_lam):
        answer2 = messagebox.askquestion("Đã làm hết tất cả câu hỏi?","Bạn có muốn nộp bài không")
    else:
        answer2 = messagebox.askquestion("Chưa làm hết câu hỏi?", "Bạn chưa làm các câu hỏi\n"+cac_cau_hoi_chua_lam+"\nbạn có muốn nộp bài không")
    if answer2=="yes":
        return True#người dùng quyết định nộp bài
    else:
        return False#người không nộp bài


def start_timer(thoigianlambai):
    global thoigiandelambai
   
    # Hàm countdown sẽ giảm thời gian và cập nhật giao diện sau mỗi giây.
    def countdown():
        global thoigiandelambai
        if thoigiandelambai == 0:
            return
        # Giảm thời gian đi một đơn vị.
        thoigiandelambai -= 1
        phut = thoigiandelambai // 60
        giay = thoigiandelambai % 60
        if giay < 10:
            giay = "0" + str(giay)
        # Cập nhật nhãn với thời gian còn lại.
        thoigianlambai.config(text=f"{phut}:{giay}")
       
        # Nếu thời gian đã hết, hiển thị thông báo thất bại.
        if thoigiandelambai == 0:
            show_failure_message()
            return
       
        # Gọi lại hàm countdown sau 1 giây.
        root.after(1000, countdown)
   
    # Bắt đầu đếm ngược.
    countdown()


def chuyen_cau_hoi(n,co_phai_xem_lai_khong=False):
    global a,b,c,d,cau_hoi,stt,canvas,csdl,screen_width,screen_height,image,tg_chuyen_cau_hoi,bo_qua,is_on,button_exit,button_setting, button_next,thoigiandelambai,sl_ch,biencamco
    global dulieu,stt,lui,dau,stt_cauhoi

    co=True

    if stt+n<=0:
        co=False
        lui.destroy()
        dau.destroy()
    if stt>0:
        lui.destroy()
        dau.destroy()


    stt=stt+n
    dulieu=csdl[stt]
    mau_nen_cua_nut=["white","white","white","white"]
    if int(dulieu[6])!=0 and not co_phai_xem_lai_khong:
        mau_nen_cua_nut[int(dulieu[6])-1]="yellow"




    cauhoi= dulieu[0]
    dap_an_a= dulieu[1]
    dap_an_b= dulieu[2]
    dap_an_c= dulieu[3]
    dap_an_d= dulieu[4]
    dapan=dulieu[5]
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    cau_hoi.destroy()
    bo_qua.destroy()
    stt_cauhoi.destroy()
    root.update()


    text_cauhoi=cauhoi
    dap_an_a= dulieu[1]
    dap_an_b= dulieu[2]
    dap_an_c= dulieu[3]
    dap_an_d= dulieu[4]
    dapan=dulieu[5]
    cau_hoi=Label (canvas,text=text_cauhoi,font=("Times New Roman",9),bg="white",width=int(screen_width*5.3)//100,height=screen_height//115)
    cau_hoi.place(x=10,y=screen_height*6//100)
    root.update()
    stt_cauhoi=Label (canvas,text=stt+1,width=int(screen_width/300),font=("Times New Roman",9),bg="yellow")
    stt_cauhoi.place(x=0,y=0)
    #nếu số lượng câu hỏi khác1 và câu hỏi hiện tại không phải câu cuối cùng thì tạo ra nút chuyển tiếp câu hỏi
    if sl_ch!=1 and stt!=sl_ch-1 :
        bo_qua=Button(canvas,text=">>",font=("Arial",9),command= lambda :chuyen_cau_hoi(1,co_phai_xem_lai_khong),bg="#DDA0DD",activebackground="yellow", width=screen_width//400,relief="flat", borderwidth=0)
        bo_qua.place(x=screen_width*50//100,y=screen_height*1/100)
    #nếu không phai câu đầu tiên thì tạo nút chuyển về câu hỏi trước và nút chuyển đến câu hỏi đầu tiên
    if stt!=0 and co:
        lui=Button(canvas,text="<<",font=("Arial",9),command= lambda :chuyen_cau_hoi(-1,co_phai_xem_lai_khong),bg="#DDA0DD",activebackground="yellow", relief="flat",width=screen_width//400, borderwidth=0)
        lui.place(x=screen_width*38//100,y=screen_height*1/100)
        dau=Button(canvas,text="|<",font=("Arial",9),command = lambda :chuyen_cau_hoi(-stt,co_phai_xem_lai_khong),bg="#DDA0DD",activebackground="yellow",width=screen_width//400, relief="flat", borderwidth=0)
        dau.place(x=screen_width*26//100,y=screen_height*1/100)
    #tạo các cấu trả lời
    a = RoundedButton(
        canvas,
        text=dap_an_a,
        radius=100,
        width=screen_width,
        height=screen_height *15// 100,
        btnbackground=mau_nen_cua_nut[0],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(a, "1", dapan)
    )
    a.place(x=0,y=screen_height*40//100)
   
    b = RoundedButton(
        canvas,
        text=dap_an_b,
        radius=100,
        width=screen_width,
        height=screen_height*15/100,
        btnbackground=mau_nen_cua_nut[1],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(b, "2", dapan)
    )
    b.place(x=0,y=screen_height*55//100)

    c = RoundedButton(
        canvas,
        text=dap_an_c,
        radius=100,
        width=screen_width,
        height=screen_height*15/100,
        btnbackground=mau_nen_cua_nut[2],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(c, "3", dapan)
    )
    c.place(x=0,y=screen_height*70//100)
   
    d = RoundedButton(
        canvas,
        text=dap_an_d,
        radius=100,
        width=screen_width,
        height=screen_height*15/100,
        btnbackground=mau_nen_cua_nut[3],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(d, "4", dapan)
    )
    d.place(x=0,y=screen_height*85/100)
    #màu nền cho các nút câu trả lời
    a.config(bg="#FF3478")
    b.config(bg="#FF3478")
    c.config(bg="#FF3478")
    d.config(bg="#FF3478")
    #nếu đang trong chế độ xem lại thì vô hiệu 4 nút trên để người dùng không chọn được mà chỉ có thể xem đồng thời đổi màu cho chúng
    if co_phai_xem_lai_khong:
        vo_hieu_4_nut()
   
        if csdl[stt][6]=='1':
            a.doimau("#FF3300","black")
        elif csdl[stt][6]=='2':
            b.doimau("#FF3300","black")
        elif csdl[stt][6]=='3':
            c.doimau("#FF3300","black")
        elif csdl[stt][6]=='4':
            d.doimau("#FF3300","black")
       
        if csdl[stt][5]=='1':
            a.doimau("#00FF33","black")
        elif csdl[stt][5]=='2':
            b.doimau("#00FF33","black")
        elif csdl[stt][5]=='3':
            c.doimau("#00FF33","black")
        elif csdl[stt][5]=='4':
            d.doimau("#00FF33","black")
    root.update()


#hàm dùng để trộn các câu hỏi và câu trả lời
def tron(arr):
    a=random.randint(1,4)
    if(a==1):
        arr[int(arr[5])],arr[1]=arr[1],arr[int(arr[5])]
        arr[5]="1"
        values=[arr[2],arr[3],arr[4]]
        random.shuffle(values)
        arr[2],arr[3],arr[4]=values
    elif(a==2):
        arr[int(arr[5])],arr[2]=arr[2],arr[int(arr[5])]
        arr[5]="2"
        values=[arr[1],arr[3],arr[4]]
        random.shuffle(values)
        arr[1],arr[3],arr[4]=values
    elif(a==3):
        arr[int(arr[5])],arr[3]=arr[3],arr[int(arr[5])]
        arr[5]="3"
        values=[arr[1],arr[2],arr[4]]
        random.shuffle(values)
        arr[1],arr[2],arr[4]=values
    else:
        arr[int(arr[5])],arr[4]=arr[4],arr[int(arr[5])]
        arr[5]="4"
        values=[arr[1],arr[2],arr[3]]
        random.shuffle(values)
        arr[1],arr[2],arr[3]=values
    return arr

#khi chưa làm bài khai báo số thứ tự của câu chuẩn bị làm là 0
stt=0
def main(co_phai_xem_lai_khong=False):

    global stt,a,b,c,d,cauhoi,cau_hoi,canvas,csdl,screen_width,screen_height,image,tg_chuyen_cau_hoi,bo_qua,is_on,button_exit,button_setting, button_next,thoigiandelambai,sl_ch,biencamco
    global dulieu,button_lui,button_dau,dau,lui,stt_cauhoi,SO_LUONG_CAU_TRA_LOI_DUNG,stop_flag
    #nếu người dùng chọn trộn câu hỏi và đang trong chế độ làm bài chương trình sẽ trộn câu hỏi và 4 câu trả lời
    if is_on and not co_phai_xem_lai_khong:
   
        for i in range(len(csdl)):
            csdl[i]=tron(csdl[i])
        random.shuffle(csdl)
    #tạo dùng canvas
    canvas = Canvas(root,width=screen_width,height=screen_height,bg="#FF3478")
    canvas.place(x=0,y=0)      
    #lấy dữ liệu ra
    dulieu=csdl[stt]
    cauhoi= dulieu[0]
    text_cauhoi=cauhoi
    dap_an_a= dulieu[1]
    dap_an_b= dulieu[2]
    dap_an_c= dulieu[3]
    dap_an_d= dulieu[4]
    dapan=dulieu[5]
    #hiển thị câu hỏi ,số thứ tự câu hỏi và 4 phương án trả lời
    cau_hoi=Label (canvas,text=text_cauhoi,font=("Times New Roman",9),bg="white",width=int(screen_width*5.3)//100,height=screen_height//115)
    cau_hoi.place(x=0,y=screen_height*6//100)


    stt_cauhoi=Label (canvas,text=stt+1,width=int(screen_width/300),font=("Times New Roman",9),bg="yellow")
    stt_cauhoi.place(x=0,y=0)
    mau_nen_cua_nut=["white","white","white","white"]
    if int(dulieu[6])!=0:
        mau_nen_cua_nut[int(dulieu[6])-1]="yellow"
    a = RoundedButton(
        canvas,
        text=dap_an_a,
        radius=100,
        width=screen_width,
        height=screen_height *15// 100,
        btnbackground=mau_nen_cua_nut[0],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(a, "1", dapan)
    )
    a.place(x=0,y=screen_height*40//100)
   
    b = RoundedButton(
        canvas,
        text=dap_an_b,
        radius=100,
        width=screen_width,
        height=screen_height*15/100,
        btnbackground=mau_nen_cua_nut[1],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(b, "2", dapan)
    )
    b.place(x=0,y=screen_height*55//100)

    c = RoundedButton(
        canvas,
        text=dap_an_c,
        radius=100,
        width=screen_width,
        height=screen_height*15/100,
        btnbackground=mau_nen_cua_nut[2],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(c, "3", dapan)
    )
    c.place(x=0,y=screen_height*70//100)
   
    d = RoundedButton(
        canvas,
        text=dap_an_d,
        radius=100,
        width=screen_width,
        height=screen_height*15/100,
        btnbackground=mau_nen_cua_nut[3],
        btnforeground="black",
        clicked=lambda: chuyen_sang_cau_hoi_tiep_theo(d, "4", dapan)
    )
    d.place(x=0,y=screen_height*85/100)
    #màu nền cho các nút câu trả lời
    a.config(bg="#FF3478")
    b.config(bg="#FF3478")
    c.config(bg="#FF3478")
    d.config(bg="#FF3478")
    #nếu đang trong chế độ xem lại thì vô hiệu 4 nút trên để người dùng không chọn được mà chỉ có thể xem đồng thời đổi màu cho chúng
    if co_phai_xem_lai_khong:
        vo_hieu_4_nut()
   
        if csdl[stt][6]=='1':
            a.doimau("#FF3300","black")
        elif csdl[stt][6]=='2':
            b.doimau("#FF3300","black")
        elif csdl[stt][6]=='3':
            c.doimau("#FF3300","black")
        elif csdl[stt][6]=='4':
            d.doimau("#FF3300","black")
       
        if csdl[stt][5]=='1':
            a.doimau("#00FF33","black")
        elif csdl[stt][5]=='2':
            b.doimau("#00FF33","black")
        elif csdl[stt][5]=='3':
            c.doimau("#00FF33","black")
        elif csdl[stt][5]=='4':
            d.doimau("#00FF33","black")
        stop_flag = False
    #nút phá màn hình
    xoa=Button(canvas,text="X",font=("Arial",9),command = tat_chuong_trinh,bg="red",activebackground="yellow", relief="flat", borderwidth=0)
    xoa.place(x=screen_width*87/100,y=screen_height*1/100)

    #nút cài đặt
    cd=Button(canvas,text="CĐ",font=("Arial",9),command= tao_cd,bg="red",activebackground="yellow", relief="flat", borderwidth=0)
    cd.place(x=screen_width*65//100,y=screen_height*1/100)
    #dùng câu lệnh rẽ nhánh để tìm câu trả lời
    if dapan=="1" :
        nut2=a
    elif dapan=="2":
        nut2=b
    elif dapan=="3":
        nut2=c
    elif dapan=="4":
        nut2=d
    #nếu số lượng câu hỏi khác 1 và đang ở câu số 2 về sau thì tạo nút chuyển câu hỏi
    if sl_ch!=1 and stt!=2:
        bo_qua=Button(canvas,text=">>",font=("Arial",9),command= lambda :chuyen_cau_hoi(1,co_phai_xem_lai_khong),bg="#DDA0DD",activebackground="yellow", width=screen_width//400,relief="flat", borderwidth=0)
        bo_qua.place(x=screen_width*50//100,y=screen_height*1/100)
    #nút nộp bài liên kết với hàm Nop_Bai, nếu đang xem lại thì văn bản trên nút là "Q.LẠI"
    nop_bai=Button(canvas,text="Q.LẠI" if co_phai_xem_lai_khong else "NỘP BÀI",command=lambda :Nop_Bai(co_phai_xem_lai_khong),width=screen_width//200,font=("Arial",9))
    nop_bai.place(x=screen_width*7//100,y=screen_height*1/100)
    #nếu người dùng có lựa chọn thời gian làm bài thì gọi biến start_timer
    if(biencamco):
        thoigianlambai=Label(root,text="",font=("Arial",8),bg="white",width=screen_width*2//250,height=screen_height//900)
        thoigianlambai.place(x=(screen_width*86//100),y=screen_height*6/100)
        start_timer(thoigianlambai)
    root.update()
    root.mainloop()




csdl= copy.copy(csdl_goc)#copy dữ liệu từ csdl gốc
tg_chuyen_cau_hoi=0


root=Tk()
#thông số màn hình bằng thông số màn hình thiết bị
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()
root.geometry(f"{screen_width}x{screen_height}")
#mặc định sẽ chuyển câu hỏi
is_on = True
#Hàm để người dùng thiết lập làm trắc nghiệm
def menu():
    global box_tg, so_luong_cau_hoi, on_button, is_on
    # Tạo canvas và đặt các thuộc tính.
    canvas = Canvas(root, width=screen_width, height=screen_height, bg="#FF3478")
    canvas.place(x=0, y=0)
    canvas2 = Canvas(canvas, width=screen_width, height=screen_height*60//100, bg="white")
    canvas2.place(x=0, y=screen_height*15//100)

    # Tạo nút để đóng cửa sổ.
    xoa = Button(canvas, text="X", font=("Arial", 22), command=tat_chuong_trinh, bg="red", activebackground="yellow", relief="flat", borderwidth=0)
    xoa.place(x=screen_width*80//100, y=screen_height*3//100)

    # Tiêu đề của ứng dụng.
    ten = Label(canvas, text="ỨNG DỤNG TRẮC NGHIỆM", font=("Arial", 13), fg="red", width=int(screen_width*1.5/50), height=int(screen_height/400), bg="white")
    ten.place(x=screen_width*2//100, y=screen_height*18//100)

    # Giao diện chọn thời gian chuyển câu hỏi.
    Label(canvas, text="Thời gian chuyển câu hỏi\nkhi làm bài(giây)", font=("Arial", 9), bg="white").place(x=screen_width*2//100, y=screen_height*34//100)
    tg = ['0', '1', '2', '3', '4', '5', '6', '7']
    box_tg = Combobox(canvas, font=("Arial", 9), width=screen_width//100, values=tg, state="readonly")
    box_tg.place(x=screen_width*64//100, y=screen_height*35/100)
    box_tg.set(tg_chuyen_cau_hoi)  # Đặt giá trị mặc định.

    # Giao diện cho việc bật/tắt trộn câu hỏi.
    Label(canvas, text="Trộn câu hỏi", font=("Arial", 9), bg="white").place(x=screen_width*2//100, y=screen_height*44//100)
    on_button = Button(canvas, text="ON", bd=0, bg="white", activebackground="white", command=switch)
    on_button.place(x=screen_width*55//100, y=screen_height*44/100)

    # Giao diện chọn thời gian làm bài.
    Label(canvas, text="Thời gian làm bài (phút)", font=("Arial", 9), bg="white").place(x=screen_width*2/100, y=screen_height*51//100)
    tglambai=["Không giới hạn",5,10,15,20,25,30,40,50,60,70,80,90,100,120]
    tg_lam_bai = Combobox(canvas, font=("Arial", 9), width=screen_width*2//100, values=tglambai, state="readonly")
    tg_lam_bai.place(x=screen_width*55//100, y=screen_height*51/100)
    tg_lam_bai.set(tglambai[0])  # Đặt giá trị mặc định.

    # Giao diện nhập số lượng câu hỏi.
    so_luong_cau_hoi = StringVar(value=str(len(csdl_goc)))
    Label(canvas, text="Số lượng câu hỏi", font=("Arial", 9), bg="white").place(x=screen_width*2//100, y=screen_height*58//100)
    Entry(canvas, font=("Arial", 9), bg="white", textvariable=so_luong_cau_hoi, width=screen_width//200).place(x=screen_width*55/100, y=screen_height*58//100)
    Label(canvas, text=f"(>0;<={len(csdl_goc)})", font=("Arial", 9), bg="white").place(x=screen_width*62/100, y=screen_height*58//100)

    # Nút bắt đầu làm bài.
    bat_dau = Button(canvas, text="BẮT ĐẦU", font=("Arial", 9), width=int(screen_width/150), height=int(screen_height/400), command=lambda: ktinput(so_luong_cau_hoi.get(), tg_lam_bai, box_tg.get()))
    bat_dau.place(x=screen_width//2-screen_width//300*16, y=screen_height*64//100)

# Gọi hàm menu để hiển thị giao diện.
menu()

#vòng lặp chính
root.mainloop()   
