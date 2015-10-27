import PyPDF2
import csv
import string
import numpy
import unicodedata
import time
from pandas import *

files = ['24x7-learning.pdf', '2coms-consulting.pdf', 'AIAEF.pdf', 'AKGEC-Skill-Pvt-Ltd.pdf', 'ASMACS-Skill-Development-Ltd..pdf', 'AVTEG Pvt Ltd.pdf', 'Abbey_West_Services_Private_Limited.pdf', 'Academy- Maritime-Education-Training-(AMET)-Trust.pdf', 'Ace-Skill-Development.pdf', 'Aegis-Skills-Edge.pdf', 'Aelis-Enterprise-Learning-Implementation-Pvt-Ltd.pdf', 'AlmaMate.pdf', 'Ambuja-Cement-Foundation.pdf', 'Anuna.pdf', 'Anytime-Learning.pdf', 'Arrina_Education_Services.pdf', 'AscensiveEducare.pdf', 'Asian-Paints.pdf', 'AssocomIndiaPvtLtd_1.pdf', 'Big Concepts Foundation Pvt. Ltd (JCRE Skill Solutions).pdf', 'Big-Animation-India-Pvt-Ltd.pdf', 'Biomed_Academy_LLP.pdf', 'Brainware-Consulting.pdf', 'Britti_Prosikshan_Pvt_Ltd.pdf', 'CAIT-Edusys-Private-Limited.pdf', 'CEDMAP.pdf', 'CIDC.pdf', 'CSC e-Governance Services India Limited.pdf', 'Cap-Workforce-Development-Institute(CAP-WDI).pdf', 'Chitkara-College-Sales-Retail-Marketing.pdf', 'Cinema_Vision.pdf', 'Cradle Life Sciences Private Limited.pdf', 'Daksha-Skill-Development-Pvt-Ltd.pdf', 'Datapro.pdf', 'Deep-Training-Institute-Pvt-Ltd.pdf', 'Delphi-Computers.pdf', 'Deshpande_Educational_Trust.pdf', 'Dhanush EnggServices.pdf', 'Dialogue in the Dark.pdf', 'Dinabandhu_Foundation_for_Educational_Research.pdf', 'Domestic Workforce Services Pvt Ltd [Compatibility Mode].pdf', 'E Herex Technologies.pdf', 'EOI_Cultural_Skill_Mapping.pdf', 'Earnest-HR-Solutions-Private-Limited.pdf', 'Employability Skills Training to rural youth in India.pdf', 'Empower-Pragati-Vocational-Staffing-Private-Limited.pdf', 'Exterior_Interior_Limited(EXIN).pdf', 'F-Tec Skilling India.pdf', 'Focus-4-D-Career-Education-Pvt.pdf', 'Frankfinn_Aviation_Services.pdf', 'GTTI.pdf', 'Global-Talent-Track-Private-Limited(GTT).pdf', 'Globsyn-Technologies-Limited.pdf', 'Gram Tarang Employability Training Services Pvt. Ltd.pdf', 'Gram-Utthan.pdf', 'HCL TalentCare Private Limited.pdf', 'Heraud Training & Education.pdf', 'Hindustan-Soft-Education.pdf', 'ICA-Edu-Skills-Pvt-Ltd.pdf', 'ICEPL.pdf', 'IIB-Education-Private-Limited.pdf', 'IMS-Proschoo-Online-Pvt-Ltd.pdf', 'ISPTVT.pdf', 'ISTAR.pdf', 'ITRC-Technologies-Pvt-Ltd.pdf', 'Indus-Edutrain-Private-Ltd.pdf', 'Indus-tree-Crafts-Foundation.pdf', 'Institute-Advance-Security-Training-Management-Private-Limited-(ASTM).pdf', 'Institute-Advance-Security-Training-Management.pdf', 'Institute-Solar-Power-Technologies-Vocational-Training-(ISPTVT).pdf', 'Interactive Institute of Job Skills (IIJS) Private Limited.pdf', 'Involute-Institute-Industrial-Training-Private-Limited.pdf', 'JITM-Skills-Private-Limited.pdf', 'Jaya_Organic_Yojna.pdf', 'Jetking-Info-train-Limited.pdf', 'K11_Fitness_Management_Company_Private_Limited.pdf', 'KVM-Academy-Pvt-Ltd.pdf', 'Kapston-Facilities-Management-Pvt-Ltd.pdf', 'KarmYog Education Network Pvt. Ltd.pdf', 'Kashi Vishwanatha Vidya Samsthe (Milaap).pdf', 'Kherwadi Social Welfare Association.pdf', 'Khwahish_Leather_Skill_Trainers_and_Consultants.pdf', 'Kohinoor-Technical-Institute.pdf', 'LaDegain-Solutions-Private-Limited.pdf', 'Laqsh-Job-Skills-Academy-Private-Limited.pdf', 'Leather Learning Solution.pdf', 'Lok Bharti.pdf', 'MIHER.pdf', 'Madura-Micro-Education-Private-Limited.pdf', 'Mahindra-Namaste.pdf', 'Meiyur-Agricultural-Training.pdf', 'Mind-Q-Academy-Private-Limited.pdf', 'Mitcon-Consulting-Engineering.pdf', 'My_Recharge.pdf', 'Nalanda-Institute-Computer-Vocational-Training.pdf', 'Nettur-Technical-Training-Foundation.pdf', 'Nidan_Technologies_Pvt_Ltd.pdf', 'PC Training Institute Ltd.pdf', 'PIPALTREE VENTRURES PRIVATE LIMITED.pdf', 'Para Medical Technology Society of India.pdf', 'Pinnnacle-Skills.pdf', 'PositiveShift_Change_Consulting_Private_Limited.pdf', 'Possit-Skill-organization.pdf', 'Power-Empower-Skills.pdf', 'ProlificSystems_TechnologiesPvtLtd.pdf', 'Quivan.pdf', 'Rozagar_Vikas_Education_Private_Limited.pdf', 'Rural-Shores-Skills-Academy-Pvt-Ltd.pdf', 'Rustomjee_Academy_for_Global_Careers_Pvt_Ltd.pdf', 'SAHAJ-e-VILLAGE-LIMITED.pdf', 'SEED-Infotech-Ltd.pdf', 'SM_Charitable_Educational_Trust.pdf', 'SPPSCT.pdf', 'SSEPL Skills Development Project.pdf', 'SUN-Skills-NSDC-Proposal.pdf', 'SV-EduSports-Private-Limited.pdf', 'SWACA.pdf', 'Safeducate.pdf', 'Sahayog-Micromanagement.pdf', 'Samta Khadi Gramodyog Sansthan (Samta).pdf', 'Sanskrit-Institutions.pdf', 'SasaKawa India Leprosy Foundation.pdf', 'ShriMahila SEWA Sahkari Bank Ltd.pdf', 'Skill Pro.pdf', 'Skill-Tree-Consulting(P)Limited.pdf', 'Skills-Academy-Private-Limited.pdf', 'Skills-Root-Edutech-Consulting.pdf', 'Society-for-Child-Development(SFCD).pdf', 'Sofcon.pdf', 'SonaYukti.pdf', 'Speakwell-Skills-Academy-Private-Limited.pdf', 'Sunrise Computer Systems Pvt. Ltd..pdf', 'Suraj_Narayan_Uchh_Takniki_Shikshan_Sansthan.pdf', 'Surgeforth Technologies Pvt Ltd.pdf', 'Syadwad-Jain-Educational-Social-Trust.pdf', 'TCI_Institute_of_Logistics.pdf', 'TUV-Rheinland-NIFE-Academy-Private-Limited.pdf', 'TalentSprint Teachers Choice.pdf', 'Unifiers-Social-Ventures-Private-Limited.pdf', 'VAG-Info-Tech-Private-Limited.pdf', 'Vidya Skills.pdf', 'Virinchi.pdf', 'Vision_india_staffing_private_limited.pdf', 'Yashaswi-Academy-Skills.pdf', 'access-livelihoods.pdf', 'aisect.pdf', 'amass-skill-ventures (1).pdf', 'ants-consulting.pdf', 'anudip-foundation.pdf', 'apollo-med-skills.pdf', 'aptech.pdf', 'arunim.pdf', 'aspiring-minds.pdf', 'avon-management.pdf', 'avr-edge.pdf', 'b-able.pdf', 'best-first-step.pdf', 'calance-software.pdf', 'caravan-craft-retail.pdf', 'centum.pdf', 'credai.pdf', 'delphi-skill-dev.pdf', 'don-bosco-tech-society.pdf', 'drishtee.pdf', 'edubridge.pdf', 'edulight.pdf', 'emergelearning.pdf', 'epam-leaf.pdf', 'esms-esource-consulting.pdf', 'future-india.pdf', 'future.pdf', 'gols.pdf', 'gras.pdf', 'i-skill.pdf', 'iPrimed-Education-Solutions-Pvt-Ltd.pdf', 'iahv.pdf', 'icss.pdf', 'iigj.pdf', 'iijt.pdf', 'iisd.pdf', 'il-fs-education.pdf', 'jbs-academy.pdf', 'jobskills.pdf', 'kalyani-skills.pdf', 'keertika.pdf', 'labournet.pdf', 'laurus-edutech.pdf', 'liqvid.pdf', 'ls-talent.pdf', 'manipal-city-guilds.pdf', 'mann-deshi-udyogini.pdf', 'microspin-machine-works.pdf', 'niit.pdf', 'nshm-skills.pdf', 'orion-edutech.pdf', 'parfi.pdf', 'pratham.pdf', 'premier.pdf', 'providers-business-academy.pdf', 'reliance-aims.pdf', 'rooman-technologies.pdf', 'saksham.pdf', 'salt-lake.pdf', 'sb-global-educational-resources.pdf', 'skill-sonics.pdf', 'skill-ventures.pdf', 'skillsource.pdf', 'smart-edusol.pdf', 'star-banker.pdf', 'sutra-tri-tech.pdf', 'synchroserve.pdf', 'talentsprint.pdf', 'the-unbeatable-india.pdf', 'tmi.pdf', 'tvs.pdf', 'value-hub.pdf', 'vidyanta.pdf']

tp_list = list()
tp_name = list()
tp_name_check = list()
tp_states = list()
tp_trainees = list()
tp_cost = list()
tp_no_centres = list()
tp_fields = list()




j=0

for i in files:
	pdfFileObj = open('./pdfs_from_site_150924/'+i, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
	num_pages = pdfReader.getNumPages()

	pageObj = pdfReader.getPage(0)
	# list with all information from pdf files
	tp_list.append(pageObj.extractText())
	
	
	if num_pages>0:
		for page in range(1, num_pages):
			pageObj = pdfReader.getPage(page)
			# list with all information from pdf files
			tp_list[j] = tp_list[j] + pageObj.extractText()


	tp_list[j] = unicodedata.normalize("NFKD", tp_list[j]).encode('ascii','ignore')
	tp_list[j] = tp_list[j].replace('\n', '')

	# Used for debugging
	#print j
	#print i
	#print ""
	#print tp_list[j]
	#print ""
	#print ""

	if i!='Ace-Skill-Development.pdf' and i!='Aegis-Skills-Edge.pdf' and i!='Aelis-Enterprise-Learning-Implementation-Pvt-Ltd.pdf' and \
	   i!='AlmaMate.pdf' and i!='Anytime-Learning.pdf' and i!='AscensiveEducare.pdf' and i!='Asian-Paints.pdf' and \
	   i!='Brainware-Consulting.pdf' and i!= 'CSC e-Governance Services India Limited.pdf' and i!= 'Cinema_Vision.pdf' and \
	   i!='Delphi-Computers.pdf' and i!= 'EOI_Cultural_Skill_Mapping.pdf' and i!= 'ICA-Edu-Skills-Pvt-Ltd.pdf' and \
	   i!='IMS-Proschoo-Online-Pvt-Ltd.pdf' and i!= 'KVM-Academy-Pvt-Ltd.pdf' and i!='Kohinoor-Technical-Institute.pdf' and \
	   i!='MIHER.pdf' and i!= 'Meiyur-Agricultural-Training.pdf' and i!= 'Nalanda-Institute-Computer-Vocational-Training.pdf' and \
	   i!='Pinnnacle-Skills.pdf' and i!= 'Power-Empower-Skills.pdf' and i!= 'SEED-Infotech-Ltd.pdf' and \
	   i!='SasaKawa India Leprosy Foundation.pdf' and i!= 'Skills-Root-Edutech-Consulting.pdf' and i!= 'SonaYukti.pdf' and \
	   i!='arunim.pdf' and i!= 'avr-edge.pdf':

		# name of organisation
		name_start = 1
		try:
			name_end = tp_list[j].index('Proposing')
		except ValueError:
			name_end = tp_list[j].index('Project')
	
		tp_name.append(tp_list[j][name_start:name_end])
		tp_name[j] = tp_name[j].strip()
	
	
		# getting second entry of org name as a check
		try:
			name_start_check = tp_list[j].index('Proposing')
		except ValueError:
			name_start_check = tp_list[j].index('Project')

		try:
			name_end_check = tp_list[j].index('No')
		except ValueError:
			name_end_check = name_start_check + len(tp_name[j])
		
		tp_name_check.append(tp_list[j][name_start_check:name_end_check])

		tp_name_check[j] = tp_name_check[j].replace('Organization ', '')
		tp_name_check[j] = tp_name_check[j].replace('Organization', '')
		tp_name_check[j] = tp_name_check[j].replace('Proposing ', '')
		tp_name_check[j] = tp_name_check[j].replace('Proposing', '')
		tp_name_check[j] = tp_name_check[j].strip()


		# in many cases 
		if  tp_name_check[j]!=tp_name[j] and tp_name_check[j]=='Access Livelihoods Consulting India Private LimitedImplementingAgencyAccess Livelihoods Consulting India Private Limited':
				tp_list[j] = tp_list[j].replace('Access Livelihoods Consulting India Private LimitedImplementingAgencyAccess Livelihoods Consulting India Private LimitedNo. of Trainees in 10 years299,016No. of Centres36centersLocation(s)Orissa, Gujarat, WestBengal and BiharSectors TargetedCo-operativesSector and Agriculture Green Business SectorProject CostRs. 30,93,00,000SourcingModelApplicant would target advertisements in the newspapers in local languages andEnglish as a key sourcing channelWomen Development Department-GOTN, Women Self Help Groups (SHGs) andthe NGOs in the State would be involved in identifying suitable candidates for thetraining programSelection of students would be based on Age, Educational qualification, incomegroup and aptitude for learning the courseA personal interview would be conducted by a selection committee set up by theAMET University for the purpose of recruiting candidates for the training programApplicant would also promote self-employment through collaboration with Banks/Government Agencies', '')
		

	
		# getting information on states targetted
		if i=='Dinabandhu_Foundation_for_Educational_Research.pdf' or i=='caravan-craft-retail.pdf' or \
		   i=='future-india.pdf' or i=='microspin-machine-works.pdf':
			tp_states.append("")

		else:
			try:
				states_start = tp_list[j].index('Location')
			except ValueError:
				states_start = tp_list[j].index('location')
			
			states_end = tp_list[j].index('Sectors')
			
			tp_states.append(tp_list[j][states_start:states_end])
			tp_states[j] = tp_states[j].replace('Location(s)', '')
			tp_states[j] = tp_states[j].replace('locations', '')
			tp_states[j] = tp_states[j].replace('location', '')
			tp_states[j] = tp_states[j].replace('Location', '')
			tp_states[j] = tp_states[j].replace(':', '')
			tp_states[j] = tp_states[j].replace('(s)', '')
			tp_states[j] = tp_states[j].replace(' Targeted', '')
			tp_states[j] = tp_states[j].replace('Targeted', '')

			tp_states[j] = tp_states[j].strip()

	
		# number of trainees
		if i=='Deshpande_Educational_Trust.pdf' or i=='Dinabandhu_Foundation_for_Educational_Research.pdf' or \
		   i=='Kashi Vishwanatha Vidya Samsthe (Milaap).pdf' or i=='Sunrise Computer Systems Pvt. Ltd..pdf' or \
		   i=='Surgeforth Technologies Pvt Ltd.pdf' or i=='microspin-machine-works.pdf':
			tp_trainees.append("")
		else:
			try:
				trainees_start = tp_list[j].index('years')
			except ValueError:
				trainees_start = tp_list[j].index('Trainees')

			try:
				trainees_end = tp_list[j].index('Centres')
			except ValueError:
				try:
					trainees_end = tp_list[j].index('Centers')
				except ValueError:
					trainees_end = trainees_start + 10
	
			tp_trainees.append(tp_list[j][(trainees_start+5):trainees_end])
			tp_trainees[j] = tp_trainees[j].replace('No. of', '')
			tp_trainees[j] = tp_trainees[j].replace('No.of', '')
			tp_trainees[j] = tp_trainees[j].replace('No of', '')
			tp_trainees[j] = tp_trainees[j].replace('over a period of 10 years', '')
			tp_trainees[j] = tp_trainees[j].replace('in 10 years', '')
			tp_trainees[j] = tp_trainees[j].strip()

	
		# Cost to NSDC
		if i=='Deshpande_Educational_Trust.pdf' or i=='Dinabandhu_Foundation_for_Educational_Research.pdf' or \
		   i=='Rustomjee_Academy_for_Global_Careers_Pvt_Ltd.pdf' or i=='gols.pdf':
			tp_cost.append("")
		else:
			cost_start = tp_list[j].index('Cost')
			try:
				cost_end = tp_list[j].index('Model')		
			except ValueError:
				try: 
					cost_end = tp_list[j].index('Sourcing')		
				except ValueError:
					cost_end = tp_list[j].index('Proposal')		

			tp_cost.append(tp_list[j][cost_start:cost_end])
			tp_cost[j] = tp_cost[j].replace('Cost', '')
			tp_cost[j] = tp_cost[j].replace('Rs.', '')
			tp_cost[j] = tp_cost[j].replace('Rs', '')
			tp_cost[j] = tp_cost[j].replace('Sourcing', '')
			tp_cost[j] = tp_cost[j].replace('Business', '')
			tp_cost[j] = tp_cost[j].replace('Revenue', '')
			tp_cost[j] = tp_cost[j].replace('(Total)', '')
			tp_cost[j] = tp_cost[j].replace('Operating', '')

			tp_cost[j] = tp_cost[j].strip()

	
		# Number of Training Centres
		if i=='Deshpande_Educational_Trust.pdf' or i=='Dinabandhu_Foundation_for_Educational_Research.pdf' or \
		   i=='Kashi Vishwanatha Vidya Samsthe (Milaap).pdf' or i=='Rustomjee_Academy_for_Global_Careers_Pvt_Ltd.pdf' or \
		   i=='Sunrise Computer Systems Pvt. Ltd..pdf' or i=='Surgeforth Technologies Pvt Ltd.pdf' or \
		   i=='caravan-craft-retail.pdf' or i=='future-india.pdf' or i=='microspin-machine-works.pdf' or \
		   i=='tmi.pdf':
			tp_no_centres.append("")
		else:
			try:
				centre_start = tp_list[j].index('entres')
			except ValueError:
				centre_start = tp_list[j].index('enters')
			
			try:
				centre_end = tp_list[j].index('Location')
			except ValueError:
				centre_end = tp_list[j].index('location')
		
			tp_no_centres.append(tp_list[j][(centre_start+6):centre_end])
			tp_no_centres[j] = tp_no_centres[j].replace('1Self-Managed-20/Franchisee-184 Total 204', '204')
			tp_no_centres[j] = tp_no_centres[j].replace('Own 1Partner  16', '17')
			tp_no_centres[j] = tp_no_centres[j].replace('250Skill Development (SDCs) & 75 Skill Development Institutes (SDIs)', '325')
			tp_no_centres[j] = tp_no_centres[j].replace('One in PuneLti()P', '1')
			tp_no_centres[j] = tp_no_centres[j].replace('20 self-managedand 80 franchise-runsatellite', '100')
			tp_no_centres[j] = tp_no_centres[j].replace('1 self-owned and 57 franchisee', '58')
			tp_no_centres[j] = tp_no_centres[j].replace('1Centre of Excellence, 2 Regional Centers and 13 Learning Centers', '16')

			tp_no_centres[j] = tp_no_centres[j].replace('No. of Centres', '')
			tp_no_centres[j] = tp_no_centres[j].replace('No of Centers', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Centers', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Centres', '')
			tp_no_centres[j] = tp_no_centres[j].replace('centers', '')
			tp_no_centres[j] = tp_no_centres[j].replace('centres', '')
			tp_no_centres[j] = tp_no_centres[j].replace("Centre's", '')
			tp_no_centres[j] = tp_no_centres[j].replace('over a period of 10 years', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Structure of Centre Centre owned by self as well as those provided by State Government and PSUs will be used for training', '')
			tp_no_centres[j] = tp_no_centres[j].replace('(6 fixed and 12 mobile)', '')
			tp_no_centres[j] = tp_no_centres[j].replace('across four locations by end of 3rdyear', '')
			tp_no_centres[j] = tp_no_centres[j].replace('(23 self owned + 46 franchisee)', '')
			tp_no_centres[j] = tp_no_centres[j].replace('States', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Self-Managed  20Franchisee  184', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Focused Learning Companies proposed in pilot phase', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' across India', '')
			tp_no_centres[j] = tp_no_centres[j].replace('in10 years', '')
			tp_no_centres[j] = tp_no_centres[j].replace('(already existing)', '')
			tp_no_centres[j] = tp_no_centres[j].replace('(2 existing and 8 new)', '')
			tp_no_centres[j] = tp_no_centres[j].replace('training', '')
			tp_no_centres[j] = tp_no_centres[j].replace('(including 2 self-owned )', '')
			tp_no_centres[j] = tp_no_centres[j].replace('fixed', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' (177 new and 56 existing )', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' in 10 yearsTargeted', '')
			tp_no_centres[j] = tp_no_centres[j].replace('self-owned', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Targeted', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' in 16 States', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Skill Upgradation(SUCs)', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' in 15 States', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' self-managed  with residential facility and 1 head office in Dwarka', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' Skill Schools', '')
			tp_no_centres[j] = tp_no_centres[j].replace('Total 63  in 10 years; Out of which  State Training Centre (STC) : 13  Primary Training Centre (PTC): 48  Regional Training Centre (RTC) : 1  Head Office : 1   2', '')
			tp_no_centres[j] = tp_no_centres[j].replace('classroom  and job site', '')
			tp_no_centres[j] = tp_no_centres[j].replace('(Acquisition55; Greenfield157; Franchisee 328; TOT/Advanced Training 6)', '')
			tp_no_centres[j] = tp_no_centres[j].replace('-', '')
			tp_no_centres[j] = tp_no_centres[j].replace(' stand-alone gurukuls(including add-on trades) and 4 Multi-skill gurukulsTargeted', '')
			tp_no_centres[j] = tp_no_centres[j].replace(':', '')
			tp_no_centres[j] = tp_no_centres[j].replace('+ (multiple  in each cluster)', '')
			tp_no_centres[j] = tp_no_centres[j].replace('  in 10 years; Jobshops 10  Jobshops+ JobAcademies 24 ; RozgarKendras 24   ', '')


			self_owned_start = tp_no_centres[j].find('(')
			self_owned_string = tp_no_centres[j][self_owned_start:len(tp_no_centres[j])]
			tp_no_centres[j] = tp_no_centres[j].replace(self_owned_string, '')
			
			tp_no_centres[j] = tp_no_centres[j].strip()

	
		# Fields of Training	
		if i == 'microspin-machine-works.pdf':
			tp_fields.append("")
		else:
			fields_start = tp_list[j].index('Targeted')
			try:
				fields_end = tp_list[j].index('Project')
			except ValueError:
				fields_end = tp_list[j].index('Proposal')

			tp_fields.append(tp_list[j][fields_start:fields_end])
			tp_fields[j] = tp_fields[j].replace('Targeted', '')

			tp_fields[j] = tp_fields[j].strip()


	else:
		tp_name.append(i)
		tp_name_check.append("")
		tp_states.append("")
		tp_trainees.append("")
		tp_cost.append("") 
		tp_no_centres.append("") 
		tp_fields.append("") 


	j=j+1



# making Pandas DataFrame of all fields collected in order to save as .csv
data = {'tp_list': tp_list, 
		'files': files,
		'tp_name': tp_name,
		'tp_name_check': tp_name_check,
		'tp_states': tp_states,
		'tp_trainees': tp_trainees,
		'tp_cost': tp_cost,
		'tp_no_centres': tp_no_centres,
		'tp_fields': tp_fields,
		}

df = DataFrame(data)

filename =  'nsdc_partners_list_' + time.strftime("%Y%m%d") + '.csv'
df.to_csv(filename, sep=',') # saved as .csv in "..../Desktop/nsdc_partners_list" with current date in filename

