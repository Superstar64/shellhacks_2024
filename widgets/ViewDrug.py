from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QVBoxLayout,
    QTableWidgetItem
)

class ViewDrug(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'List of Drugs'
        self.database = database

    def update(self):
        data = []
        for (id, drug, pharamacy) in self.database.execute('select drug_id, drug_type.name, pharmacies.name from inventory, drug_type, pharmacies where drug_type.id = drug_type_id and pharmacies.id = pharmacy_id'):
            data.append ((id, drug, pharamacy))
        
        table = QTableWidget(len(data), 3)
        index = 0
        for (id, drug, pharamacy) in data:
            table.setItem(index, 0, QTableWidgetItem(str(id)))
            table.setItem(index, 1, QTableWidgetItem(str(drug)))
            table.setItem(index, 2, QTableWidgetItem(str(pharamacy)))
            index += 1

        box = QVBoxLayout()
        box.addWidget(table)

        self.setLayout(box)