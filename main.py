from turtle import width
import dataTreatment as data
import plot


def main():
    departamentos = data.total_victims[f'total_victims_DEPARTAMENTO']
    años = data.total_victims[f'total_victims_ANIO_HECHO']
    etapa = data.total_victims[f'total_victims_ETAPA']
    edad = data.total_victims[f'total_victims_GRUPO_EDAD_VICTIMA']
    sex = data.total_victims[f'total_victims_SEXO_VICTIMA']

    total_cases_edad = data.count_cases('GRUPO_EDAD_VICTIMA')
    victims_per_cases = data.count_cases('TOTAL_VICTIMAS')
    sex_per_cases = data.count_cases('SEXO_VICTIMA')

    municipio_victims_per_year = data.calculate_two_related_values_victims(
        'ANIO_HECHO', 'MUNICIPIO')
    departamento_victims_per_year = data.calculate_two_related_values_victims(
        'ANIO_HECHO', 'DEPARTAMENTO')
    age_cases_per_year = data.calculate_two_related_values_cases(
        'ANIO_HECHO', 'GRUPO_EDAD_VICTIMA')
    age_victims_per_year = data.calculate_two_related_values_victims(
        'ANIO_HECHO', 'GRUPO_EDAD_VICTIMA')

    active_cases_per_year = data.calculate_two_related_cualitative_values(
        'ANIO_HECHO', "ESTADO_NOTICIA", "ACTIVO")

    condenados_per_year = data.calculate_two_related_cualitative_values(
        'ANIO_HECHO', 'CONDENA', 'SI')
    captures_per_year = data.calculate_two_related_cualitative_values(
        'ANIO_HECHO', 'CAPTURA', 'SI')
    acussed_per_year = data.calculate_two_related_cualitative_values(
        'ANIO_HECHO', 'ACUSACION', 'SI')

    plot(departamentos, "Número de víctimas por departamento", "Departamentos",
         "Victimas")
    plot(edad, "victimas por edad", "Grupo edad", "Víctimas")
    plot(total_cases_edad, "casos por edad", "Grupo edad", "Casos")
    plot(victims_per_cases, "casos por número de victimas",
         "Número de victimas", "Casos")

    for year in ["2015", "2016", "2017", "2018", "2019", "2020"]:
        dictionary_plot = {}
        for key in departamento_victims_per_year:
            if (year in key):
                temp_key = ' '.join(key.split()[2:])
                dictionary_plot[temp_key] = departamento_victims_per_year[key]
        plot.vbar(dictionary_plot, f"victimas por departamento en {year}",
                  "Departamento", "Víctimas")

    plot.vbar(sex, "victimas por sexo", "sexo", "Víctimas")
    plot.vbar(sex_per_cases, "casos por sexo", "sexo", "Casos")
    años = dict(sorted(años.items(), key=lambda item: item[0]))
    plot.vbar(años, "victimas por año", "Año", "Victimas")


if __name__ == "__main__":
    main()
