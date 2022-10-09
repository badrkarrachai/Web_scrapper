from autoscraper import AutoScraper
import xlsxwriter

# Creating models

# url = 'https://youth.europa.eu/volunteering/organisations_en?country=DE&topic=&scope%5Bql%5D=&town=&name=&combine=&inclusion_topic=&field_eyp_vp_feweropp_additional_mentoring_1=&field_eyp_vp_feweropp_additional_physical_environment_1=&field_eyp_vp_feweropp_additional_other_support_1=&field_eyp_vp_feweropp_other_support_text=&&op=Apply%20Filter&page=23'
# # We can add one or multiple candidates here.
# # You can also put urls here to retrieve urls.
# wanted_list = ["478"]
# scraper = AutoScraper()
# result = scraper.build(url, wanted_list)
# print(result)
# scraper.save('number.json')
# del scraper

# Using Models
Countries = ['AL','AM','AT','AZ','BA','BE','BG','BY','CH','CY','CZ','DE','DK','DZ','EE','EG','EL','ES','FI','FR','GE','GL','HR','HU','IE','IL','IS','IT','JO','LB','LI','LT','LU','LV','MA','MD','ME','MK','MT','NC','NL','NO','PL','PS','PT','RO','RS','RU','SE','SI','SK','TN','TR','UA','UK','XK']
CountriesFullName = ["[AL] Albania", "[AM] Armenia", "[AT] Austria", "[AZ] Azerbaijan", "[BA] Bosnia and Herzegovina", "[BE] Belgium", "[BG] Bulgaria", "[BY] Belarus", "[CH] Switzerland", "[CY] Cyprus", "[CZ] Czech Republic", "[DE] Germany", "[DK] Denmark", "[DZ] Algeria", "[EE] Estonia", "[EG] Egypt", "[EL] Greece", "[ES] Spain", "[FI] Finland", "[FR] France", "[GE] Georgia", "[GL] Greenland", "[HR] Croatia", "[HU] Hungary", "[IE] Ireland", "[IL] Israel", "[IS] Iceland", "[IT] Italy", "[JO] Jordan", "[LB] Lebanon", "[LI] Liechtenstein", "[LT] Lithuania", "[LU] Luxembourg", "[LV] Latvia", "[MA] Morocco", "[MD] Moldova (Republic of)", "[ME] Montenegro", "[MK] North Macedonia", "[MT] Malta", "[NC] New Caledonia", "[NL] Netherlands", "[NO] Norway", "[PL] Poland", "[PS] Palestine", "[PT] Portugal", "[RO] Romania", "[RS] Serbia", "[RU] Russian Federation", "[SE] Sweden", "[SI] Slovenia", "[SK] Slovakia", "[TN] Tunisia", "[TR] Turkey", "[UA] Ukraine", "[UK] United Kingdom", "[XK] Kosovo UN resolution"]
countIndex = 0
for country in Countries:
    workbook = xlsxwriter.Workbook("data/"+CountriesFullName[countIndex]+".xlsx")
    countIndex=countIndex+1
    worksheet = workbook.add_worksheet(country)
    scraper = AutoScraper()
    scraper.load('number.json')
    url2 = "https://youth.europa.eu/volunteering/organisations_en?country="+country+"&topic=&scope%5Bql%5D=&town=&name=&combine=&inclusion_topic=&field_eyp_vp_feweropp_additional_mentoring_1=&field_eyp_vp_feweropp_additional_physical_environment_1=&field_eyp_vp_feweropp_additional_other_support_1=&field_eyp_vp_feweropp_other_support_text=&&op=Apply%20Filter&page=0"
    result = scraper.get_result_similar(url2)
    try:
        pages = int(int(result[0])/20)+1
    except:
        workbook.close()
        continue
    rowIndex=0
    del scraper
    for x in range(pages):
        scraper = AutoScraper()
        scraper.load('medium.json')
        url2 = "https://youth.europa.eu/volunteering/organisations_en?country="+country+"&topic=&scope%5Bql%5D=&town=&name=&combine=&inclusion_topic=&field_eyp_vp_feweropp_additional_mentoring_1=&field_eyp_vp_feweropp_additional_physical_environment_1=&field_eyp_vp_feweropp_additional_other_support_1=&field_eyp_vp_feweropp_other_support_text=&&op=Apply%20Filter&page="+str(x)
        result = scraper.get_result_similar(url2)
        for row in result:
            s = "".join(map(str, row))
            if s.startswith("https://") or s.startswith("http://"):
                worksheet.write(rowIndex,0,s)
                print('A'+str(rowIndex),0,s+'\n')
            else:
                worksheet.write(rowIndex,0,"https://"+s)
                print('A'+str(rowIndex),"https://"+s+'\n')
            rowIndex=rowIndex+1
        del scraper
    print('--------------------'+country+'--------------------')
    workbook.close()




