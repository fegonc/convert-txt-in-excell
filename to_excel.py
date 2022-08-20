import pandas as pd

joblist = []
app_list = []
desc_list = []

with open('tws_opc.txt', 'r') as file:
      fh = file.readlines()
      irofile = iter(fh)

      for i in irofile:
            if "APPLICATION" in i:
                app_list.append(i.split(':')[1].replace('\n', ''))
            elif "DESCRIPTIVE" in i:
                desc_list.append(i.split(':')[1].replace('\n', ''))
            elif "JOB NAME" in i:
                joblist.append(i.split(':')[1].replace('\n', ''))
                while(True):
                    try:
                        i = next(irofile)
                        if "JOB NAME" in i:
                            joblist.append(i.split(':')[1].replace('\n', ''))
                            desc_list.append('')
                            app_list.append('')
                        else:
                            app_list.append(i.split(':')[1].replace('\n', ''))
                            break

                    except StopIteration:

                        d = {'APP NAME': app_list, 'DESCRIPTION': desc_list, 'JOB NAME': joblist}

                        df = pd.DataFrame.from_dict(d, orient='index')
                        df = df.transpose()

                        # Exporting dataframe to Excel file
                        df.to_excel("converted-to-excel.xlsx")

                        writer = pd.ExcelWriter('converted-to-excel.xlsx')
                        df.to_excel(writer)
                        writer.save()

                        break






























































