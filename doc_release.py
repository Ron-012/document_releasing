# A clear text-based main menu
# Add, insert, or register a record
# Process, update, release, return, or delete a record as appropriate to the chosen system
# Display all records currently stored in the program
# Search Record option using linear search; binary search may be added only for sorted records
# Proper input validation and readable output formatting
# Continuous program loop until the user chooses Exit

# 1. Add Request
# 2. Process / Update
# 3. Release Document
# 4. Return Document
# 5. Search Record
# 6. Display Records
# 7. Delete Record
# 8. Exit

# START PROGRAM
import datetime as dt
import random
import string     

def generate_doc_id():
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"DOC-{timestamp}-{suffix}"

def update_doc(records):
  while True:
    doc_id = input("Enter Document ID: ")
    
    found = False # set to false unless found

    for record in records:
      if record["ID"] == doc_id:

        found = True # found

        print(f"\nCurrent details: \n" # info in records
              f"ID: {record["ID"]}\n"
              f"Document Name: {record["Document Name"]}\n"
              f"Requester: {record["Requester"]}\n"
              f"Status: {record["Status"]}\n")
        
        record["Document Name"] = input("New Document Name: ") # infos that can be changed
        record["Requester"] = input("New Document Requester: ")
        break
    
    if not found: # not found
      print("Document not found")
      
    again = input("Try Again? (y/n): ").lower() # try
    if again == "y":
      continue
    else:
      break

def change_status(records, stats):
   doc = input("\nEnter Document ID: ")
    
   for record in records:
    if record['ID'] == doc:
        
      record['Status'] = stats
      print(f"Document has been {stats}.")
      return
    
   print("Document not found.")

def delete_record(records):
   doc_id = input("\nEnter Document ID to delete: ")

   for i, record in enumerate(records): # get index and value
    if record['ID'] == doc_id:
        
      records.pop(i)
      print(f"Document {doc_id} has been deleted.")
      return
    
   print("Document not found.")

records = []

while True:

  print('\n===== DOCUMENT RELEASING SYSTEM =====')
  print('1) Register Document') 
  print('2) Update / Release / Return / Delete Document')
  print('3) Display All Documents')
  print('4) Search Document')
  print('5) Exit')

  select = int(input('\nSelect a number (1-5): '))
  
  if select == 1: #register
    id = generate_doc_id()
    name = input('\nDocument Name: ')
    req = input('Requester Name: ')
    date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status = 'Pending'    

    new_record = {
     'ID': id,
     'Document Name': name,          # creates new record
     'Requester': req,
     'Date Requested': date,
     'Status': status
    }

    records.append(new_record) #adds new record

    print('\nDocument successfully registered.')
    print('Document ID:', id )

#----------------------------------------------------
  
  elif select == 2: #update/release/return/delete
    if len(records) == 0:
      print('\nNo records available')
      continue

    else:
      print('\n1) Update \n' \
      '2) Release \n' \
      '3) Return \n' \
      '4) Delete'
      )

      choice = int(input('\nSelect a number (1 - 4): '))

#----------------------------------------------------
        
      if choice == 1: # updating document
        update_doc(records)
  
      elif choice == 2:
        change_status(records, 'Released')

      elif choice == 3:
        change_status(records, 'Returned')

      elif choice == 4:
        delete_record(records)
        
# --------------------------------------------------------

  elif select == 3:
    if len(records) == 0:
       print('No records stored.')

    else:
      for record in records:
        print("\n------------------------------------------")
        print("Document ID:", record["ID"])
        print("Document Name:", record["Document Name"])
        print("Requester:", record["Requester"])
        print("Date Requested:", record['Date Requested'])
        print("Status:", record["Status"])
        print("------------------------------------------")

#-------------------------
    
  elif select == 4:
    search = input("\nEnter Document ID: ")

    found = False

    for record in records:
      if record["ID"] == search:
        print("\n------------------------------------------")
        print("Document ID:", record["ID"])
        print("Document Name:", record["Document Name"])
        print("Requester:", record["Requester"])
        print("Date Requested:", record['Date Requested'])
        print("Status:", record["Status"])
        print("------------------------------------------")
        found = True
        break
    
    if not found:
      print("Record not found")
        
  elif select == 5:
    print("\nExiting program...")
    break

  else:
    print("Invalid input. Please try again")
