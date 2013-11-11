import sys
import clr
clr.AddReferenceToFileAndPath(r'C:\app\SOME_WINDOWS_USER\product\11.2.0\client_1\ODP.NET\bin\2.x\Oracle.DataAccess.dll')
clr.AddReference("System.Data")
from Oracle.DataAccess.Client import OracleConnection, OracleDataAdapter
from System.Data import DataTable
from System import Exception as exce

tableName = sys.argv[1]

strcon = r'Data Source=SOME_SOURCE;User Id=SOME_USER;Password=SOME_PASSWORD'
oracon = OracleConnection(strcon)
dt = DataTable()
qry = "select * from {} where 1 = 2".format(tableName)
try:
	adtr = OracleDataAdapter(qry, oracon)
	adtr.Fill(dt)
	for col in dt.Columns:
	  print "{} {}".format(col.ColumnName, col.DataType.FullName)
except exce as e:
	print  e.Message
	
