from django.shortcuts import render
import pickle
import os
import pandas as pd

def predict_fertility_rate(request):
    if request.method == 'POST':
        model_filename = 'prediction.pkl'
        model_path = os.path.join(os.path.dirname(__file__), 'models', model_filename)
        
        # Load the trained model from the pickle file
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)

        # Get user input from the form
        population_2023 = request.POST.get('population_2023')
        yearly_change = request.POST.get('yearly_change')
        net_change = request.POST.get('net_change')
        density = request.POST.get('density')
        land_area = request.POST.get('land_area')
        migrants_net = request.POST.get('migrants_net')
        fert_rate = request.POST.get('fert_rate')
        med_age = request.POST.get('med_age')
        urban_pop = request.POST.get('urban_pop')

        # Check if any of the fields are empty
        if None in [population_2023, yearly_change, net_change, density, land_area, migrants_net, fert_rate, med_age, urban_pop]:
            return render(request, 'predict_fertility_rate.html', {'error_message': 'Please fill in all the fields.'})

        # Convert values to float
        try:
            population_2023 = float(population_2023)
            yearly_change = float(yearly_change)
            net_change = float(net_change)
            density = float(density)
            land_area = float(land_area)
            migrants_net = float(migrants_net)
            fert_rate = float(fert_rate)
            med_age = float(med_age)
            urban_pop = float(urban_pop)
        except ValueError:
            return render(request, 'predict_fertility_rate.html', {'error_message': 'Invalid input. Please enter valid numbers.'})

        test_data = pd.DataFrame({
            'Population(2023)': [population_2023],
            'YearlyChange': [yearly_change],
            'NetChange': [net_change],
            'Density(P/Km²)': [density],
            'Land Area(Km²)': [land_area],
            'Migrants(net)': [migrants_net],
            'Med.Age': [med_age],
            'UrbanPop %': [urban_pop]
        })

        # Make prediction
        prediction = model.predict(test_data)[0]

        # Render the result
        return render(request, 'prediction_result.html', {'prediction': prediction})

    # If the form is not submitted, render the empty form
    return render(request, 'predict_fertility_rate.html')
