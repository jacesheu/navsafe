from flask import (Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import numpy as np

# Create and configure the app
app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev')

# Load data from the model
df = pd.read_csv('flaskr/static/final_prediction_agg_10.csv', index_col=0)
df = df[df.pred==1] # keep information on areas to avoid

# Route for the home page
@app.route('/', methods=('GET', 'POST'))
def map_func():
    if request.method == 'POST':
        # Retrieve user entered info
        origin = request.form['origin']
        destination = request.form['destination']
        time = request.form.get('time')
        error = None
        
        # Check for required inputs
        if not origin:
            error = 'Origin is required.'
        elif not destination:
            error = 'Destination is required.'

        # Calculate areas to avoid within the active region of the route
        if error is None:
            val = 0.005
            org_latlon = list(map(float, origin.split(',')))
            dest_latlon = list(map(float, destination.split(',')))
            
            # Calculate active region of the route
            lat_min = min(org_latlon[0],dest_latlon[0])
            lat_max = max(org_latlon[0],dest_latlon[0])
            lon_min = min(org_latlon[1],dest_latlon[1])
            lon_max = max(org_latlon[1],dest_latlon[1])

            # Find top 10 relevant areas to avoid
            avoid = df[(df.NewLat.between(lat_min-val*np.sign(lat_min), lat_max+val*np.sign(lat_max))) & 
                       (df.NewLon.between(lon_min+val*np.sign(lon_min), lon_max-val*np.sign(lon_max))) & 
                       (df['Time Seg']==time)]
            avoid = avoid.sort_values('Weight', ascending=False).head(10)
            
            # Define avoid input value for the API
            avoid_list = avoid[['NewLat','NewLon']].apply(lambda x: 'bbox:' + str(x['NewLon']-0.00125) + 
                                                          ',' + str(x['NewLat']-0.00125) + ',' + str(x['NewLon']+0.00125) + 
                                                          ',' + str(x['NewLat']+0.00125), axis=1).values
            avoid_param = '|'.join(avoid_list)
            avoid_lat = ','.join([str(lat) for lat in avoid.NewLat]) 
            avoid_lon = ','.join([str(lon) for lon in avoid.NewLon]) 

            return render_template('map_sf_route.html', 
                                   org_input=origin, 
                                   org_dest=destination, 
                                   time=time,
                                   avoid_bbox=avoid_param,
                                   avoid_lat=avoid_lat,
                                   avoid_lon=avoid_lon)
        
    return render_template('map_sf.html')

if __name__ == '__main__':
    app.run(debug = True)    