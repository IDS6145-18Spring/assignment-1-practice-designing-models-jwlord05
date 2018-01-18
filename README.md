# Assignment1 - Practice Designing Models (Template)


> * Participant name: John Lord
> * Project Title: A Smart City Creates Green Space; Can the U.S. implement "Super Blocks"?

## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smart_city_green_space.jpg)

A Smart City promotes the health and prosperity of its citizenry.    Eliminating vehicular traffic in urban areas allows for the creation of green space used primarily by pedestrians.  Fewer cars on the roadway means reduced carbon emissions, increased oxygen intake, increased safety and an overall boost to public health both mentally and physically.  There appear to be almost no negative aspects of car free urban areas.  The question becomes, for cities in the US that were built around the extensive use of vehicular traffic; Can modern resources be used efficiently enough to make spending money on transforming urban culture worth the effort.  Electronic means can be used to monitor and manage public assets such as public transportation (rail lines), business deliveries, pedestrian and bike traffic and outside commuter parking.

Cities all oever the world have already implemented car free zones.  In Madrid, Spain, the Super Block implementation is a step toward pedestrianizing the central urban areas. Paris, France reduced overal carbon emmissions by 30% by reducing the number of cars and increasing Cities all oever the world have already implemented car free zones.  In Madrid, Spain, the Super Block implementation is a step toward pedestrianizing the central urban areas. Paris, France reduced overal carbon emmissions by 30% by reducing the number of cars and increasing public bike assess.  Chengdu, China is reducing vehicular traffic in urban areas with the promiss it will take only 15 min to transverse the car free zone, reducing overall "stalled in traffic" concerns.  Hamburg, Germany has plans to create a green network by reducing cars and inclreasing parks and reducing already croweded traffic systems.  These are just a few of the cities with reduced public bike assess.  Chengdu, China is reducing vehicular traffic in urban areas with the promiss it will take only 15 min to transverse the car free zone, reducing overall "stalled in traffic" concerns.  Hamburg, Germany has plans to create a green network by reducing cars and inclreasing parks and reducing already croweded traffic systems.  These are just a few of the real-world examples.

The benefits of car free zone are exemplary: increased use of public transportation, reduction of carbon emissions, increase of oxygen levels, increase physical and mental health of city residents, increased safety.  The problem set this paper will explore is the timeframe necessary to traverse car free zones utilizing: public transportation such as a train or bus, bike lanes and/or walking.

Source:
https://www.theguardian.com/sustainable-business/2015/apr/20/garden-cities-can-green-spaces-bring-health-and-happiness
http://smartgrowth.org/6-urban-green-space-projects-that-are-revitalizing-u-s-cities/
https://www.youtube.com/watch?v=ZORzsubQA_M

## Requirements (Experimental Design)

(remove: You should start by specifying a set of requirements. I specified a topic Smart Cities but what exactly does that mean-  you should practice formulating your own set of requirements and an experiment. Define a hypothesis of a problem cities face and how a smart city would possibly help alleviate this issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

A major problem cities face is overcrowding, pollution and lack of recreation.  The flip side is access to urban areas.  This paper proposes the following experiment.  Can the creation of green space be conducted while still maintaining a reasonable access?  The requirements follow:
1)  Given an urban area of (n) size wherein all the streets are closed to public traffic.
2)  Given public transportation is available (scalable) in the same area.
     a)  Public transportation includes public tram (electric/natural gas) with variable routes through area.
          1 - tram includes THREE cars (can vary?)
          2 - tram can carry 25 comuters per car
          3 - tram can travel 15 mph
     b)  public bike rentals available at variable locations throughout area
          1 - bikes can only carry ONE passanger
          2 - bikes can only travel 5 mph
          3 - bikes can only travel on bike path
     c)  Public bike/pedestrian paths delineated throughout area (set)
          1 - pedestrians can only travel on pedestrian path
          2 - pedestrians can only travel 2.5 mph
3)  Commuter debarkation points set; no more than four (4)
4) Public interaction random AND set  -- population (p) size feasible for area (n) of consideration!
     a)  random population living within urban area traversing area from point A (home) to point B (work)
     b)  random population commute to debarkation point (parking garage) and traversing area from point A (parking garage) to point B (work)
     c)  random population utilizing green space with no start or end destination
     c)  All population randomly utilizing three modes of transpiration: 1) walking paths, 2) bike lanes (rental bikes) 3) public tram
5)  Population movement times set
     a)  small percentage (10%) of population movement constantly between 0600-2300 –represents misc population
     b)  random percentage (15-30%) of population movement between 0900-2300  -- represents population utilizing businesses and green space
     c)  working population (55%) movement between 0630-0900 (morning), 1130-1300 (lunch), and 1430-1730 (evening)
6)  All buildings within (n) area identified
     a) office buildings
     b) residential buildings
     c) lunch/dinner/entertainment building
7)  Must compute and report average time for commuters to traverse from point A to point B

## Smart City (My Problem) Model

The idea is to model a green space within an urban area in order to simulate the time it takes for commuters to travel from the "commuter hub" to their respective (random) employment locations.  Within the model it is necessary to provide resources wihtin the green zone for transportation and competing entity requirements for the resources.  The resources modeled are pedestrian paths, bike paths and tram paths.  The competing entities are shoppers (MISC) and residents.

* [**Object Diagram**](model/object_diagram_green.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram_green.md) - provides details of verables and functions related to the Object Diagram

These diagrams are not used (Behavior and Agent)

* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## Smart City (My Problem) Simulation

The attached MD file explains what type of simluation is used and why: [**John Lord**](analysis/John Lord.md) 


## Smart City (My Problem) Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.


From code to diagram.  This is an intitial/simplified attempt to take the POTS code (given by instructor) and convert it back to a [class](http://www.google.com) diagram [**POTS Class Diagram**](code/green_city/POTS_class_diagram.png) 