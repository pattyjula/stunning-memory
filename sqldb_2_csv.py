# Import libraries
import csv
import pypyodbc

# Set connections
conn = pypyodbc.connect('Driver={SQL Server};'
                                'Server=pdw;'
                                'Database=db_name;'
                                'uid=readonly;pwd=readonly')
# Create a cursor
crsr = conn.cursor()

# Use NOLOCK
SQLCommand = """\
SELECT TOP (20000) [DR]
      ,[actNo]
      ,[ts]
      ,[CrmDate]
      ,[RptDate]
      ,[StatDate]
      ,[RD]
      ,[RptDiv]
      ,[RptDivCD]
      ,[InvDiv]
      ,[InvDivCD]
      ,[PrimCC]
      ,[AllCC]
      ,[Stat]
      ,[NumSusp]
      ,[MOCodes]
      ,[PrimWpn]
      ,[Narrative]
      ,[lat]
      ,[lon]
      ,[crmEnd]
      ,[crmGrp]
  FROM [compStat].[dbo].[Crime] NOLOCK
"""

# Execute command
rows = crsr.execute(SQLCommand)

# Save to CSV
with open(r'staging/compStat_crime_draft.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([x[0] for x in crsr.description])  # column headers
    for row in rows:
        writer.writerow(row)

print(SQLCommand)
conn.close() # Close connection