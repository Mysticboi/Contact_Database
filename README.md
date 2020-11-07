# Contact_Database
Creating a contact database using Python and SQLite. To run the program run contact.py.

## Menu
When the programs starts(database is empty) the user can choose 1 of this 4 options available:
  * 1: Inserting into the database : The program then asks for 4inputs: name,adress,phone and email. Then it's added into the Contact Table.
  * 2: Finding a contact: The program asks for a name input:
    * If the name is found, returns the full informations of the contact.
    * If the name is not found, warns the user.
  * 3: Deleting a contact: The program asks for a name input:
    * If the name is found, deletes the contact.
    * If the name is not found, warns the user.
  * 4: Updating a contact: The program asks for a name input:
    * If the name is found, aks for a new adress,phone and email to update the contact.
    * If the name is not found, warns the user.

### Shape of the Database
The database is simple, it's composed of a single table Contact which contains 4 columns: Name, Adress,Phone and Email.
Exemple:
Name | Adress | Phone | Email
-----|--------|-------|------
Walid | 508  Michael Street | 062392101 | walid@hotmail.com
Camille | 4321  Blue Spruce Lane | 0450202303 | camille@gmail.com
Theo | 1875  Thomas Street | 062321292 | theo@outlook.com
Loris | 4476  Hiddenview Drive | 0121345560 | loris@yahoo.com
