# Canada Population Maps

This application visualizes changes in the Canadian population over 20 years using streamlit.

## To Install 

I had some issues with dependencies on Windows, but install them individually in this order worked:

```
pipenv install wheel
pipenv install pipwin
pipenv install matplotlib

pipwin install numpy
pipwin install pandas
pipwin install shapely
pipwin install gdal
pipwin install fiona
pipwin install pyproj
pipwin install six
pipwin install rtree
pipwin install geopandas
```

Below are some screenshots from the interactive Bokeh population plot, which has population change data from 2017 - 2020. Population change is calculated as the log of absolute population growth to adjust for very large spikes in growth in our largest cities. The results are pretty predictable, growth in cities and reduction in the areas surrounding them. What I was curious about was Vancouver Island, but the data shows growth across all cencus divisions.

![bokeh_plot](https://user-images.githubusercontent.com/2029528/162273269-2c091f63-5921-4a4b-9b1e-f3abc9b41005.png)
![bokeh_plot(1)](https://user-images.githubusercontent.com/2029528/162273273-79cfff40-cb42-4b4e-aed8-874a3532662d.png)
