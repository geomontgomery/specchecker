from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
import xml.etree.ElementTree as ET
import pandas as pd
import io
import datetime
import xlsxwriter
from spectools import *

def checkprj():
	prj =  file_upload("Select a *.PRJ file below to check CADWorx® to Plant3D® Convertability:", accept=".prj")
	realname = prj['filename']
	content = prj['content']
	
	tree = ET.fromstring(content)

	rows = spectools.speccrawl(tree)
	df = pd.DataFrame(rows)
	df = speccheck.addchecks(df)

	# spec tests
	df = speccheck.specblankends(df)
	df = speccheck.specblankdatatable(df)
	df = speccheck.specblankclass(df)
	df = speccheck.specblankschedule(df)
	df = speccheck.specblankmaterial(df)
	df = speccheck.spechardsd(df)
	df = speccheck.spechardld(df)
	df = speccheck.specreducingus(df)
	df = speccheck.specusdata(df)

	# formatting output
	df[['CategoryType','SortID']] = df[['CategoryType','SortID']].astype(int)
	df = df.sort_values(by=['SpecName','CategoryType','SortID'])
	dfout = df[['SpecName','Name','er1','er2','er3','er4','er5','er6','er7','er8','er9']].copy()
	dfout = dfout.reset_index(drop=True)
	# dfout = dfout.index.name='#'
	
	output = io.BytesIO()

	with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
		dfout.to_excel(writer, sheet_name='Sheet1', startrow=0, index=True) #TODO or output?

		book= writer.book
		sheet = writer.sheets['Sheet1']
		sheet.set_column('C:C',44)
		format1 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(D2:D1001="EndType")',
				"format": format1
				}
					)
		format2 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(E2:E1001="DataTable")',
				"format": format2
				}
					)
		format3 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(F2:F1001="PressureClass")',
				"format": format3
				}
					)
		format4 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(G2:G1001="ScheduleBlank")',
				"format": format4
				}
					)
		format5 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(H2:H1001="MaterialBlank")',
				"format": format5
				}
					)
		format6 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(I2:I1001="SDtypedin")',
				"format": format6
				}
					)
		format7 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(J2:J1001="LDtypedin")',
				"format": format7
				}
					)
		format8 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(K2:K1001="ReducingUS")',
				"format": format8
				}
					)
		format9 = book.add_format({'bg_color': '#E93423'})
		sheet.conditional_format("C2:C10001",
				{"type": "formula",
				"criteria": '=(L2:L1001="UsershapeData")',
				"format": format9
				}
					)
	writer.save()

	put_text(f'You just uploaded {realname}')

	dlname = realname.replace('.prj',"")
	downloadfile = str(datetime.date.today())+'-'+dlname+'-cwx-to-p3d.xlsx'
	put_text(f'Click below to download the report')
	put_file(downloadfile, output.getvalue(),label=downloadfile)

	hold()