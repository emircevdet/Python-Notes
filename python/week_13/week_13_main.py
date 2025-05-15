import week_13_functions

db = week_13_functions.sql_functions()
db.create_table()

while True:
    print("\n"\
    "1- Add Candidate\n" \
    "2- List All Candidates\n" \
    "3- Update Candidates Score by ID\n" \
    "4- Delete Candidate by ID\n" \
    "5- Find Maximum Score\n" \
    "6- Exit\n")

    menu = int(input("Select one of the choices from above: "))
    print()
    
    if menu == 1:
        candidate_id = input("\nCandidate ID: ")
        candidate_name = input("Candidate Name: ")
        test_score = int(input("Enter Test Score: "))
        test_year = int(input("Enter Test Year: "))
        db.add_candidate(candidate_id, candidate_name, test_score, test_year)
    elif menu == 2:
        db.list_candidate()
    elif menu == 3:
        update_id = input("Enter ID to be updated: ")
        new_score = int(input("Enter new test score: "))
        db.update_candidate(update_id, new_score)
    elif menu == 4:
        delete_id = input("Enter ID to be deleted: ")
        db.delete_candidate(delete_id)
    elif menu == 5:
        db.find_maximum_score()
    elif menu == 6:
        print("Logging out...\n")
        exit(0)
    else:
        print("Please enter valid option!")
