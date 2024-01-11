class Star_Cinema:
    hall_list = []
   
    def entry_hall(self,rows,cols,hall_no):
        info_of_hall_list = Hall(rows,cols,hall_no)
        self.hall_list.append(info_of_hall_list)



class Hall:
   
    def __init__(self,rows,cols,hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.check_ids = []
       
    def entry_show(self,id_no,movie_name,time):
        info_of_show = (id_no,movie_name,time)
        self._show_list.append(info_of_show)
        self.check_ids.append(id_no)
       
        seat = []
       
        for i in range(self._rows):
            seat_line = []
           
            for j in range(self._cols):
                seat_line.append('Free')
            seat.append(seat_line)
       
        self._seats[id_no] = seat  
       
   
    def book_seats(self,id_no,list_of_shows):
        try:
            if id_no in self.check_ids:
               for (x,y) in list_of_shows:
                   if x >= 0 and x <= self._rows and y >=0 and y <= self._cols:
                       if self._seats[id_no][x][y] == 'Free':
                           self._seats[id_no][x][y] = 'Booked'
                           print(f"Tickets booked for ID: {id_no} ! The seat is in ({x},{y})")
                       else:
                           print("Seats not available")
                   
                   else:
                        print("Invalid input for seats!")
                       
            else:
                print(f"ID {id_no} is not in the list of entry shows")
               
        except ValueError:
          print('Error Occured')
   
    def view_show_list(self):
        if len(self._show_list) == 0:
            print("No Show available")
        else:
            for (x,y,z) in self._show_list:
                print(f'MOVIE NAME: {y}({x}). SHOW ID: {x}. TIME: 10/1/2024 {z}.')
               
           
       
    def view_available_seats(self,id_no):
        try:
            if id_no in self.check_ids:
                f = 0
                for i in range(self._rows):
                    for j in range(self._cols):
                        if self._seats[id_no][i][j] == 'Free':
                            print(f'Available seats for ID {id_no} is ({i},{j})')
                            f = 1
               
                if f == 0:
                    print("No seats available")
               
            else:
                print(f'ID {id_no} is not available')
       
        except ValueError:
           print('Error Occured!')

class Ticket_counter:
    def __init__(self,duplicate_Hall):
        self.duplicate_Hall = duplicate_Hall
   
    def movie_entry_show(self,id_no,movie_name,time):
        self.duplicate_Hall.entry_show(id_no,movie_name,time)
   
    def movie_book_seats(self,id_no,list_of_shows):
        self.duplicate_Hall.book_seats(id_no,list_of_shows)
   
    def view_movie_show_list(self):
        self.duplicate_Hall.view_show_list()
       
    def view_available_movie_seats(self,id_no):
        self.duplicate_Hall.view_available_seats(id_no)


counter = Hall(10,10,2)

Ticket = Ticket_counter(counter)

Ticket.movie_entry_show(201,'m-2','17:00')
Ticket.movie_entry_show(202,'m-3','15:00')
Ticket.movie_entry_show(303,'m-4','11:00')
Ticket.movie_entry_show(304,'m-5','10:00')
Ticket.movie_entry_show(402,'m-5','18:00')
Ticket.movie_entry_show(404,'m-6','12:00')

while True:
    print('1. VIEW ALL SHOW TODAY.')
    print('2. VIEW AVAILABLE SEATS.')
    print('3. BOOK TICKET.')
    print('4. EXIT.')

    n = int(input("ENTER OPTION: "))

    if n == 1:
        print('-------------------')
        Ticket.view_movie_show_list()
        print('-------------------')
    elif n == 2:
        movie_id = int(input('ENTER SHOW ID: '))
        Ticket.view_available_movie_seats(movie_id)
    elif n == 3:
        movie_id = int(input("ENTER SHOW ID: "))
        t = int(input('Number of Ticket: '))
        showList = []
        for i in range(t):
            x = int(input('Seats in row: '))
            y = int(input("Seats in Column: "))
            seat = (x,y)
            showList.append(seat)
        Ticket.movie_book_seats(movie_id,showList)
    elif n == 4:
        break    

