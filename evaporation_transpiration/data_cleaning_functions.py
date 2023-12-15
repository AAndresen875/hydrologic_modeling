#observed_weather_waseca_2007
def rename_waseca_weather_columns(observed_weather_df_waseca_2007):
    """
    function to take in the dataframe: observed_weather_waseca_2007
    data exploration and data cleaning logic can be found in the notebook data_cleaning logic
    """
    #renaming dict for column in observed_weather_waseca_2007 to be single line evaluations
    observed_weather_waseca_2007_columns_rename_dict = {
        'Unnamed: 0': 'year', 
        'Unnamed: 1': 'day', 
        'Unnamed: 2': 'temp_max_celcius', 
        'Unnamed: 3': 'temp_min_celcius', 
        'Rain ': 'rain_runoff_site_mm',
        'Unnamed: 5': 'tile_site_mm', 
        'Pan Evaporation': 'pan_evaporation_observed_mm', 
        'Unnamed: 7': 'est_daily_mm', 
        'Unnamed: 8': 'radiation_megaj_msq_d',
        'Unnamed: 9': 'rhmax_percent', 
        'Unnamed: 10': 'rhmin_percent', 
        'Wind ': 'wind_speed_m_s'
    }
    observed_weather_df_waseca_2007.rename(columns=observed_weather_waseca_2007_columns_rename_dict,inplace=True)
    print("Shape of dataframe after renaming columns to be a single line evaluation description", observed_weather_df_waseca_2007.shape)
    #dropping the first two rows with unit information now in the column name: 
    observed_weather_df_waseca_2007.drop(index=[0,1],inplace=True)
    print("Shape of df after dropping the first and second row:",observed_weather_df_waseca_2007.shape)
    return observed_weather_df_waseca_2007

#Observed ET data from corn 2007
def rename_waseca_corn_columns(waseca_corn_dataframe):
    """
    This function will take in the observed_et_data_waseca_corn_r204 dataframe and export it with the columns renamed
    """
    #renaming columns and pulling off the first row:
    renaming_waseca_corn_columns = {
            'Unnamed: 0': 'year', 
            'Unnamed: 1': 'day', 
            'Soil Moisture Content': 'soil_moist_cont_20_cm', 
            'Unnamed: 3': 'soil_moist_cont_40_cm',
            'Unnamed: 4': 'soil_moist_cont_80_cm', 
            'Unnamed: 5': 'soil_moist_cont_100_cm', 
            'ET': 'et_mm',
        }
    waseca_corn_dataframe.rename(columns=renaming_waseca_corn_columns,inplace=True)
    print("Shape of df copying units into column name:", waseca_corn_dataframe.shape)
    waseca_corn_dataframe.drop(index=0,inplace=True)
    print("Shape of df after dropping the first row:",waseca_corn_dataframe.shape)
    return waseca_corn_dataframe