# NavSafe

## Problem
Anyone who has ever been in an unfamiliar city knows the feeling of apprehension that comes with navigating on foot from point to point. You want to walk to your destination efficiently, but are also mindful of the desire to stay safe. Without the embedded knowledge of being a local, you don’t know which streets to avoid, particularly in the evenings.

For certain populations such as women, this problem feels particularly acute.

Existing solutions do little to address this major issue:

- Conventional navigation apps like Google Maps don’t factor in pedestrian safety in their routing algorithms, often leading you through poorly lit alleyways to save on travel time
- Searching online on forums like Reddit is both time-consuming and confusing, as you can get conflicting information, and don’t have a great way to integrate that into your navigation plans
- Using online crime heat maps doesn’t give sufficient granularity - these tools often mark off entire neighborhoods, which isn’t useful.

## Solution
NavSafe uses historical crime statistics, data from safety surveys, and clustering models to generate an intelligence overview of dangerous areas in a city. 

Users simply has to enter: 
- Longitude & latitude of starting point
- Longitude & latitude of destination point
- Time of day (morning, afternoon, evening, or night)

Navsafe will then generate a route recommendation that is both efficient and safe. It also highlights risky areas in the map that are avoided.

## How NavSafe Works


## Running the Code

### Data Pipeline & Processing

### Modeling
In this session, we will train the model on the final data generated from the data pipeline session. The following is a description of code functions for each part.

<details>
  <summary> Load Data </summary>
</details>

<details>
  <summary> Supervised - Logistic Regression </summary>
</details>

<details>
  <summary> Unsupervised - Clustering </summary>
</details>

<details>
  <summary> Map Visualization </summary>
</details>

<details>
  <summary> Test Set Comparison </summary>
</details>

<details>
  <summary> Predict </summary>
</details>

<details>
  <summary> Route Comparison </summary>
</details>

### Web App (UI)

## References 
