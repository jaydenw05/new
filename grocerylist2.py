import tkinter
import tkinter.messagebox
import pickle
#testing
root= tkinter.Tk()
root.title("Grocery list")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title= "Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title= "Warning!", message="You must select a task")

def load_tasks():
    tasks= pickle.load(open("item_cost.txt")) 

def save_tasks():
    tasks = listbox_task.get(0, listbox_tasks.size())
    listbox_task.delete(0, tkinter.END)
    pickle.dump(tasks, open("tasks.dat", "wb"))
    
def load_list():
    class main:
        def _init_(self,item,price):
            self.item = item
            self.pruce = price
        with open("item cost.txt","r") as item_cost:
            lines = item_cost.readlines()
            items = []
            
        for l in lines:
            as_list = 1.;split(",")
            cow = main(as_list[0],as_list[1].replace("\n", ""))
            items.append(cow)
            
        for items in items:
            listbox_task.insert(tkinter.END, items.item)
            listbox_task.insert(tkinter.END, items.price)
            
        def mutiple_yview(*args):
             listbox_task.yview(*args)
             listbox_task .yview(*args)
             listbox_task .yview(*args)


# Create GUI
frame_task = tkinter.Frame(root)
frame_task.pack()
listbox_task = tkinter.Listbox(frame_task, height=10, width=50)
listbox_task.pack(side=tkinter.LEFT)

listbox_task = tkinter.Listbox(frame_task, height=10, width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)


scrollbar_task.config(command=listbox_task.yview)

item_label=tkinter.Label(text= "Price")
item_label.pack()
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

item_label=tkinter.Label(text= "Item")
item_label.pack()
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()


button_add_task = tkinter.Button(root, text= "add task", width=48, command=add_task)
button_add_task.pack()

button_add_task = tkinter.Button(root, text= "delete task", width=48, command=add_task)
button_add_task.pack()

button_add_task = tkinter.Button(root, text= "load task", width=48, command=add_task)
button_add_task.pack()

button_add_task = tkinter.Button(root, text= "save task", width=48, command=add_task)
button_add_task.pack()

root.mainloop()

