import pandas as pd
import matplotlib.pyplot as plt

# se crea una serie temporal con una fecha de inicio, el número de periodos y la frecuencia
dates = pd.date_range('2016/10/29 5:30pm', periods=12, freq='H')
print(dates)

# se crea una serie temporal de números decimales 
# y se le añaden las fechas anteriores para tener una serie de datos con índices
temperatures = [4.4,5.1,6.1,6.2,6.1,6.1,5.7,5.2,4.7,4.1,3.9,3.5]
temp_series = pd.Series(temperatures, dates)
print(temp_series)

# se interpola una segunda serie con una frecuencia diferente
temp_series_freq_30min = temp_series.resample("30Min").interpolate(method="cubic")

# se muestran ambas series temporales en el mismo gráfico
temp_series.plot(label="Periodo: 1 hora")
temp_series_freq_30min.plot(label="Periodo: 30 min")
plt.legend()
plt.grid(True)
plt.show()

# con tz_localize se asigna una zona horaria a una serie temporal
temp_series_ny = temp_series.tz_localize("America/New_York")
print(temp_series_ny)

# se puede transformar entre zonas horarias con el tz_convert
temp_series_paris = temp_series_ny.tz_convert("Europe/Paris")
print(temp_series_paris)

# con period_range en lugar de una fecha se usan cuatrimestres
quarters = pd.period_range('2016Q1', periods=8, freq='Q')
print(quarters)

# aún así puedes transformar entre los dos formatos usando to_timestamp para fechas
time_stamps = quarters.to_timestamp(how="end", freq="H")
print(time_stamps)


# y usando to_period para volver a los cuatrimestres
time_stamps.to_period()


# DATOS CATEGÓRICOS

# creamos una dataframe con valores que representan categorías
df = pd.DataFrame({
    "sexo": {"alice": "F", "bob": "H", "charles": "H"}
})

print("DataFrame original:")
print(df)

# añadimos una nueva columna a partir de la columna de categorías
df["sexo_cat"] = df["sexo"].astype('category')

print("\nDataFrame con columna 'sexo_cat' como categoría:")
print(df)

# cambiamos la categoria de la nueva columna
df["sexo_cat"].cat.set_categories = ["Mujer", "Hombre"]
df["sexo_cat"] = df["sexo_cat"].cat.rename_categories(["Mujer", "Hombre"])

print("\nDataFrame con categorías renombradas:")
print(df)

# se crea la variable dummies en booleanos
# se convierten los booleanos a 0 y 1
# y se unen al dataframe
df_dummies = pd.get_dummies(df["sexo_cat"])
df_dummies = df_dummies.astype(int)
df = pd.concat([df, df_dummies], axis=1)

print("\nDataFrame con variables dummies añadidas:")
print(df)