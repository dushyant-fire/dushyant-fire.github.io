---
layout: page
title: Pyrolysis properties and material type
description: Research to understand the effect of PMMA type on pyrolysis properties
img: assets/img/Research_pics/cone_heater.jpeg
importance: 1
category: work
related_publications: true
---

Poly (methyl methacrylate) (PMMA) has long been a benchmark material of study in the fire research and fire modeling community due to its simple and predictable thermal decomposition behavior. Two common PMMA manufacturing processes, casting and extruding, produce polymers with slightly different properties and characteristics, primarily a result of differences in molecular mass.

A dichotomy has been observed between study and application; while cast PMMA is more commonly studied and modeled, it is extruded PMMA that has wider use and application. This study investigates the differences between cast and extruded PMMA on a property-specific level, and whether the differences justify unique pyrolysis models for each.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/Research_pics/cone_heater.jpeg" title="cone heater" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Cone Heater with a calibration heat flux gauge.
</div>

Experimental results show notable variation in milligram-scale tests such as Thermo-gravimetric Analysis (TGA), Differential Scanning Calorimeter (DSC) and Microscale combustion calorimeter (MCC), but only slight variation in gram-scale tests (Controlled Atmosphere Pyrolysis Apparatus II or CAPA II).

Comprehensive pyrolysis models are developed for each PMMA type with the help of hill climbing optimization algorithms to automate inverse analysis. A sensitivity analysis is performed on the fully parameterized models to examine the effect of prominent parameters on the model’s ability to predict mass loss rate from CAPA II tests. It is determined that the two materials are sufficiently similar to be represented with a generic model.

Check out more information in the full publication {% cite Fiola2021 %}.
