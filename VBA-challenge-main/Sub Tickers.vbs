Sub Tickers()

For Each ws In Worksheets
' Title of columns
    
    ws.Cells(1, 12).Value = "first date"
    ws.Cells(1, 13).Value = "open"
    ws.Cells(1, 14).Value = "last date"
    ws.Cells(1, 15).Value = "closed"
    ws.Cells(1, 16).Value = "yearly change"
    ws.Cells(1, 17).Value = "percentage change"
    ws.Cells(1, 18).Value = "total stock volume"

'find the last row for column a
    Dim lastRow As Long
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

'Find the unique tickers and total volume stock

    Dim tickername As String

    Dim tickertotal As String
    tickertotal = 0

    Dim column_tickername As Integer
    column_tickername = 2

    Dim column_tickertotal As Integer
    column_tickertotal = 2

    For i = 2 To lastRow
    
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
        'unique ticker
            tickername = ws.Cells(i, 1).Value
            ws.Cells(column_tickername, 11).Value = tickername
            column_tickername = column_tickername + 1
        'total volume stock
            tickertotal = tickertotal + ws.Cells(i, 7).Value
            ws.Cells(column_tickertotal, 18).Value = tickertotal
            column_tickertotal = column_tickertotal + 1
        
        Else
            tickertotal = tickertotal + ws.Cells(i, 3)
        End If
                
    Next i

' find last row for the unique ticker
    Dim Rowy As Long
    Rowy = ws.Cells(Rows.Count, 11).End(xlUp).Row

'find first date, last date, open value, closed value, yearly change, percentage change
    For j = 2 To Rowy
    'first date
        ws.Cells(j, 12).FormulaR1C1 = "=+MINIFS(C[-10],C[-11],RC[-1])"
    'last date
        ws.Cells(j, 14).FormulaR1C1 = "=+MAXIFS(C[-12],C[-13],RC[-3])"
    'open value
        ws.Cells(j, 13).FormulaR1C1 = "=+SUMIFS(C[-10],C[-12],RC[-2],C[-11],RC[-1])"
    'closed value
        ws.Cells(j, 15).FormulaR1C1 = "=+SUMIFS(C[-9],C[-14],RC[-4],C[-13],RC[-1])"
    'yearly change
        ws.Cells(j, 16).Value = ws.Cells(j, 15) - ws.Cells(j, 13)
    'yearly % change
        ws.Cells(j, 17).Value = ws.Cells(j, 15) / ws.Cells(j, 13) - 1
    'format cells green surplus, red loss
        If ws.Cells(j, 16) >= 0 Then
            ws.Cells(j, 16).Font.ColorIndex = 4
        Else
            ws.Cells(j, 16).Font.ColorIndex = 3
        End If
    
        ws.Cells(j, 17).NumberFormat = "0.00%"

    Next j

Next ws

End Sub

