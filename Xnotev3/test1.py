def addLineTable(self):

    row = self.model.rowCount()   #create a line into my tableview
    self.model.insertRows(row)
    column = 0
    index = self.model.index(row, column)        
    tableView = self.TABLE            
    tableView.setFocus()
    tableView.setCurrentIndex(index)
    cursor = self.editor.textCursor()

    # get the current format
    format = cursor.charFormat()
    # modify it
    format.setBackground(QtCore.Qt.red)
    format.setForeground(QtCore.Qt.blue)
    # apply it
    cursor.setCharFormat(format)

    textSelected = cursor.selectedText()  #set text to cursor
    self.model.setData(index, QVariant(textSelected)) #set text to new tableview line