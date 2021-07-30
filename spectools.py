class spectools:

	def speccrawl(tree):
		rows = []
		for spec in tree:
			if spec.tag == 'Specification':
				spec_name = list(spec.attrib.items())
				for comps in spec:
					if comps.tag == 'Components':
						for comp in comps:
							if comp.attrib.get('ID') == None:
								continue
							comp.attrib['SpecName'] = spec_name[1][1]
							# for userval in comp:
								# if comp.attrib.get('FACING') == None:
									# continue
								# comp.attrib['FACING'] = 
							for index, endtype in enumerate(comp):
								# facing = endtype.find('Facing')
								# if facing is None:
									# continue
								# facing = endtype.get('Facing')
								# print(facing)
								# if endtype.tag == 'ProjectUserDataTable':
								# 	userfield = list(endtype.attrib.items())
								# 	print(val)
								if endtype.tag == 'EndType':
									end_types = list(endtype.attrib.items())
									# print(end_types)
									newend = 'end'+str(index)
									newclass = 'class'+str(index)
									comp.attrib[newend] = end_types[1][1]
									comp.attrib[newclass] = end_types[3][1]
							rows.append(comp.attrib)
		return rows
	
class speccheck:


	def addchecks(df):
		df[['er1','er2','er3','er4','er5','er6','er7','er8','er9']]=''
		return df


	def specblankends(df):
		"""Checking if EndType isn't filled out in spec components. If the incoming dataframe contains -1 for end0, and ISNOT category type 5,6,9,12, then return the resulting dataframe

		Args:
		    df ([dataframe]): [input dataframe]

		Returns:
		    dfreturn ([dataframe]): [returned dataframe]
		"""
		# df[['CategoryType','SortID']] = df[['CategoryType','SortID']].astype(int)
		df.loc[(df['end0']=="-1"),'er1']="EndType"
		df.loc[((df['CategoryType']=='5') | (df['CategoryType']=='6') | (df['CategoryType']=='9') | (df['CategoryType']=='12')),'er1']=""
		# df.loc[((df['end0']=="-1") & ((df['CategoryType']!='5') | (df['CategoryType']!='6') | (df['CategoryType']!='9') | (df['CategoryType']!='12'))),'er1']="1"
		# df.loc[((df['end0']=="-1") & ((df['CategoryType']!='5') | (df['CategoryType']!='6') | (df['CategoryType']!='9') | (df['CategoryType']!='12'))),'er1']="1"
		return df
		
	def specblankdatatable(df):
		"""If the datatable isn't filled out on the component, return the resulting dataframe.

		Args:
		    df ([type]): [description]

		Returns:
		    [type]: [description]
		"""
		df.loc[df['Name']=="",'er2']="DataTable"
		return df

	def specblankclass(df):
		df.loc[df['class0']=="",'er3']="PressureClass"
		return df

	def specblankschedule(df):
		df.loc[df['MainSchedule']=="",'er4']="ScheduleBlank"
		return df

	def specblankmaterial(df):
		df.loc[df['MaterialItem_ID']=="65435",'er5']="MaterialBlank"
		return df

	def spechardsd(df):
		df.loc[df['ShortDesc']!="",'er6']="SDtypedin"
		return df

	def spechardld(df):
		df.loc[df['LongDesc']!="",'er7']="LDtypedin"
		return df

	def specreducingus(df):
		df.loc[df['Reducer']=="1",'er8']="ReducingUS"
		return df

	def specusdata(df):
		# df.loc[df['Reducer']=="1",'er8']="1"
		return df