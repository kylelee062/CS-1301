class Database:
    def __init__(self):
        self.tables = {'students': {}, 'courses': {}}
        self.next_record_id = {'students': 1, 'courses': 1}

    def add_table(self, table_name, column_values):
        record_id = self.next_record_id[table_name]
        self.tables[table_name][record_id] = column_values
        self.next_record_id[table_name] += 1
        print(f"Record added to {table_name} table with ID: {record_id}.")

    def remove_table(self, table_name, record_id):
        try:
            record_id = int(record_id)  
        except ValueError:
            print(f"ERROR: Invalid record ID '{record_id}'. Record ID must be an integer.")
            return

        if record_id in self.tables[table_name]:
            del self.tables[table_name][record_id]
            print(f"Record {record_id} removed successfully from {table_name} table.")
        else:
            print(f"ERROR: Record ID '{record_id}' not found in {table_name} table.")

    def print_all_table(self, table_name):
        print(f"All records in {table_name} table:")
        for record_id, values in self.tables[table_name].items():
            print(f"Record ID: {record_id}, Values: {values}")

    def print_specific_table(self, table_name, record_id):
        try:
            record_id = int(record_id)  
        except ValueError:
            print(f"ERROR: Invalid record ID '{record_id}'. Record ID must be an integer.")
            return

        if record_id in self.tables[table_name]:
            print(f"Record ID: {record_id}, Values: {self.tables[table_name][record_id]}")
        else:
            print(f"ERROR: Record ID '{record_id}' not found in {table_name} table.")


    def update_table(self, table_name, record_id, column_name, new_value):
        try:
            record_id = int(record_id)  
        except ValueError:
            print(f"ERROR: Invalid record ID '{record_id}'. Record ID must be an integer.")
            return

        if record_id in self.tables[table_name]:
            if column_name in self.tables[table_name][record_id]:
                self.tables[table_name][record_id][column_name] = new_value
                print(f"Record {record_id} in {table_name} table updated successfully.")
            else:
                print(f"ERROR: Column '{column_name}' not found in {table_name} table.")
        else:
            print(f"ERROR: Record ID '{record_id}' not found in {table_name} table.")


student_table = Database()
course_table = Database()

while True:
    print("\nMenu Commands:")
    print("1. Add")
    print("2. Remove")
    print("3. Print")
    print("4. Update")
    print("Type 'quit' or 'q' to exit")

    user_input = input("\nEnter: ").lower()

    if user_input in ["quit", "q"]:
        break

    if user_input in ['add', 'a']:
        table_name = input("Enter table name (students/courses): ").lower()
        if table_name in ['students', 'courses']:
            if table_name == 'students':
                column_values = {
                    'name': input("Enter name: "),
                    'address': input("Enter address: "),
                    'phone': input("Enter phone: "),
                    'email': input("Enter email: "),
                    'GPA': float(input("Enter GPA: ")),
                }
            elif table_name == 'courses':
                column_values = {
                    'course': input("Enter course: "),
                    'professor': input("Enter professor: "),
                    'semester': input("Enter semester: "),
                    'CRN': input("Enter CRN: "),
                    'grade': input("Enter grade: "),
                }

            if table_name == 'students':
                student_table.add_table(table_name, column_values)
            elif table_name == 'courses':
                course_table.add_table(table_name, column_values)
        else:
            print("Invalid table name.")


    elif user_input in ['remove', 'r']:
        table_name = input("Enter table name (students/courses): ").lower()
        if table_name in ['students', 'courses']:
            record_id = input(f"Enter record ID to remove from {table_name} table: ")
            if table_name == 'students':
                student_table.remove_table(table_name, record_id)
            elif table_name == 'courses':
                course_table.remove_table(table_name, record_id)
        else:
            print("Invalid table name.")

    elif user_input in ['print', 'p']:
        table_name = input("Enter table name (students/courses): ").lower()
        if table_name in ['students', 'courses']:
            print_option = input("Enter 'all' to print all records, 'specific' to print a specific record: ").lower()
            if print_option == 'all':
                if table_name == 'students':
                    student_table.print_all_table(table_name)
                elif table_name == 'courses':
                    course_table.print_all_table(table_name)
            elif print_option == 'specific':
                record_id = input("Enter record ID to print: ")
                if table_name == 'students':
                    student_table.print_specific_table(table_name, record_id)
                elif table_name == 'courses':
                    course_table.print_specific_table(table_name, record_id)
            else:
                print("Invalid print option.")
        else:
            print("Invalid table name.")

    elif user_input in ['update', 'u']:
        table_name = input("Enter table name (students/courses): ").lower()
        if table_name in ['students', 'courses']:
            record_id = input("Enter record ID to update: ")
            column_name = input("Enter column name to update: ")
            new_value = input("Enter new value: ")
            if table_name == 'students':
                student_table.update_table(table_name, record_id, column_name, new_value)
            elif table_name == 'courses':
                course_table.update_table(table_name, record_id, column_name, new_value)
        else:
            print("Invalid table name.")

    else:
        print("Invalid command. Please try again.")
