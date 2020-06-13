import csv 
import time

class Export:

    def __init__(self, statistics):
        self.root = "./data/exports/"
        self.name = ""
        self.HTML = ".html"
        self.CSV = ".csv"
        self.statistics = statistics
        
    def writeCSV(self):
        total_average = self.statistics[0][0].total_average(self.statistics)
        section = []
        vector = [""]
        for v in self.statistics[0]:
            vector.append(v.algorithm)
            vector.append("\t")
            vector.append("\t")
        section.append(vector)   
        vector = ["Dataset"]   
        for v in self.statistics[0]:            
            vector.append("Media")
            vector.append("Desviación")
            vector.append("Tasa de exito")
        section.append(vector)        
        for statistics in self.statistics:
            vector = []
            vector.append(statistics[0].name_file)
            for s in statistics:
                vector.append(str(round(s.average(), 3)))
                vector.append(str(round(s.std(), 3)))
                vector.append(str(round(s.successfull_rate(), 3)))
            section.append(vector)
            vector = ["Total"]
        for total in total_average:
            vector.append(str(round(total, 3)))
        section.append(vector)
        
        self.def_name()
        with open(self.root + self.name + self.CSV, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
            writer.writerows(section)

        
    def writeHTML(self):
        total_average = self.statistics[0][0].total_average(self.statistics)
        html = "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='X-UA-Compatible' content='ie=edge'><link rel='stylesheet' href='./styles/style.css'><title>Algoritmos de Estado Simple</title></head><body>"
        html += "<div class='schedule-container'><div class='schedule-title'><span>Rendimiento</span></div><div class='table-responsive'><div class='schedule-table'><table>"
        html += "<thead><tr><th rowspan='2'>Dataset</th>"
        for v in self.statistics[0]:
            html += "<th colspan='3'>" + v.algorithm + "</th>"
        html +="</tr><tr>"
        for i in self.statistics[0]:
            html += "<th>Media</th><th>Desviacion</th><th>Tasa de exito</th>"
        html += "</tr></thead><tbody>"
        for statistics in self.statistics:
            html += "<tr><td>" + statistics[0].name_file + "</td>"
            for i in range(len(statistics)):
                html += "<td class='non-select'><span>" + str(round(statistics[i].average(), 3)) + "</span></td>"
                html += "<td class='non-select'><span>" + str(round(statistics[i].std(), 3)) + "</span></td>"
                html += "<td class='non-select" + (" success'" if int(statistics[i].successfull_rate()) == 100 else "") + "'><span>" + str(round(statistics[i].successfull_rate(), 3)) + "</span></td>"
            html += "</tr>"
        html += "<tr><td>" + "TOTAL" + "</td>"
        for total in total_average:
            html += "<td class='non-select special'><span>" + str(round(total, 3)) + "</span></td>"
        html += "</tr>"

        html += "</tbody></table></div></div></div></body></html>"

        self.def_name()
        hs = open(self.root + self.name + self.HTML, 'w')
        hs.write(html)

    def def_name(self):
        self.name = "record_{}_{}".format(time.strftime("%d_%m_%y"), time.strftime("%H_%M"))
