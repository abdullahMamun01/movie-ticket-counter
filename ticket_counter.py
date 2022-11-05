from random import randint


class Star_Cinema:
    hall_list = []

    def entry_hall(self):
        pass

    def showHall(self):
        print(self.hall_list)


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        self.hall_list.append({
            "rows": self.rows,
            "cols": self.cols,
            "hall_no": self.hall_no,
            "seats": self.seats,
            "show_list": self.show_list
        })

    def entry_show(self):
        # show details
        id = input("SET SHOW ID : ")
        movie_name = input("ENTER MOVIE NAME : ")
        time = input("MOVIE STARTING TIME : ")
        self.show_list.append(
            {"id": id, "movie_name": movie_name, "time": time})
        self.seats[id] = [["empty" for r in range(self.rows)]
                          for c in range(self.cols)]
        self.generate_seat_no(id)

    def book_seats(self):
        # booking information from user
        customer_name = input("ENTER CUSTOMER NAME: ")
        customer_phone = input("ENTER PHONE NO. : ")
        show_id = input("ENTER SHOW ID : ")

        # check show id exist or not
        if (not self.isValid_id(show_id)):
            print("INVAILD SHOW_ID\n")
            return

        total_tickets = int(input("ENTER NUMBER OF TICKETS "))
        user_info = {
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "id": show_id,
            "total_tickets": []
        }
        # number of ticket input
        while (total_tickets > 0):
            ticket = input("ENTER SEAT NO ")
            self.book_seat(ticket, show_id)
            user_info["total_tickets"].append(ticket)
            total_tickets -= 1

        print("____________TICKET BOOKING SUCCESSFULLY __________\n")
        self.booking_info(user_info)

    # booking ticket seat
    def book_seat(self, ticket, id):
        flag = False
        print("\n")
        if (ticket == "X"):
            print("SORRY THIS SEAT IS ALREADY BOOKED!")
            return
        print("\n")

        for data in self.hall_list:
            if data["seats"][id]:
                for i in range(self.cols):
                    for j in range(self.rows):
                        if (data["seats"][id][i][j] == ticket):
                            data["seats"][id][i][j] = "X"
                            flag = True
                            break

        if not flag:
            print("SEAT NO. DO NOT MATCHED ")
            return

    print("\n")

    # generate random char.
    def create_random_seats_no(self):
        return "".join(chr(randint(65, 90)) for i in range(1))

    # check valid show's of id
    def isValid_id(self, id):
        flag = False
        for data in self.hall_list:
            for show in data["show_list"]:
                if show["id"] == id:
                    flag = True

        return flag

    def booking_info(self, user_info):
        # user info. from user
        print("NAME : ", user_info["customer_name"])
        print("PHONE: ", user_info["customer_phone"])
        print("TICKETS :", end="")
        for ticket in user_info["total_tickets"]:
            print(ticket, end=" ")
        print()

    # number of available seats
    def show_availabe_seats(self):
        id = input("ENTER SHOW ID : ")
        print("\n")
        flag = False
        for data in self.hall_list:
            # show movie info
            for show in data["show_list"]:
                if (show["id"] == id):
                    print("MOVIE NAME : ", show["movie_name"], end="")
                    print("\t\t TIME : ", show["time"])
                    flag = True
            if not flag:
                print("THIS SHOW ID DO NOT EXIST ")
                print("\n\n")
                return

            print("\n")
            print("x for already book")
            print(f"{'_'*60}", end="\n")
            # show seat info
            if (data["seats"][id]):
                for r in data["seats"][id]:
                    for c in r:
                        print(c, end="\t\t\t\t")
                    print("\t")
                    print()
            print(f"{'_'*60}", end="\n")

    def view_show_list(self):
        print(f"{'_'*60}")
        for data in self.hall_list:
            for show in data["show_list"]:
                print("MOVIE NAME : ", show["movie_name"], end="\t")
                print("ID : ", show["id"], end="\t")
                print("TIME : ", show["time"])

        print(f"{'_'*60}")

    # generate ranodm seat no.
    def generate_seat_no(self, id):
        for i in range(self.cols):
            for j in range(self.rows):
                self.seats[id][i][j] = f"{self.create_random_seats_no()}{i}"


s = Star_Cinema()
h = Hall(4, 3, 12)

while (True):
    print("0.EXIT ")
    print("1.ENTRY MOVIE SCHEDULE ")
    case = int(input("Enter option "))
    if (case == 0):
        break
    if case == 1:
        h.entry_show()


print("en")

while (True):
    print("1.VIEW ALL SHOW TODAY  ")
    print("2.VIEW AVAILABLE SEATS ")
    print("3.BOOKING SEATS ")
    print("0.EXIT ")
    case = int(input("ENTER OPTION : "))
    if case == 0:
        break

    if case == 1:
        h.view_show_list()
    elif case == 2:
        h.show_availabe_seats()
    elif case == 3:
        h.book_seats()
