import utils
import read_csv
import charts

def run():
  #lectura de data desde enlace
  data = read_csv.read_csv('./app/data.csv')
  #filtro con lambda para solo utilizar la columna continent
  data = list(filter(lambda item : item['Continent'] == 'South America',data))
  #mapeo de la columna country/territory 
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''

if __name__ == '__main__':
  run()