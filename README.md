# Thermography based Blood Flow Imaging

In this project we had used FLIR ONE PRO for Android for capturing thermal images. These thermal images are then processed as described in the paper "Thermography-based blood flow imaging in human skin of the hands and feet: a spectral filtering approach" by A A Sagaidachnyi et al [1].

## Dependencies

We had used *sci-kit learn, numpy, opencv, [read_thermal.py from @Nervengift](https://github.com/Nervengift/read_thermal.py)* libraries/modules for processing Thermal Images in *python3*. Mainly **read_thermal** was used for getting images with temperature in degrees celsius at each pixel location from using the header present in the captured image. The **read_thermal** internally uses **exiftool** for getting the header information from the image like *'Emissivity', 'SubjectDistance', 'AtmosphericTemperature', 'ReflectedApparentTemperature', 'IRWindowTemperature', 'IRWindowTransmission', 'RelativeHumidity', 'PlanckR1', 'PlanckB', 'PlanckF', 'PlanckO', 'PlanckR2'* which are then used to get temperature in degrees celsius.

## Procedure

An example video of blood flow of a hand is as follow <br>
<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="https://github.com/SvrAdityaReddy/Thermography_based_Blood_Flow_Imaging/blob/master/main/data_santosh/out0.jpg">
    <source src="https://github.com/SvrAdityaReddy/Thermography_based_Blood_Flow_Imaging/blob/master/main/data_santosh/s_bldf.avi" type="video/avi">
  </video>
</figure>

The entire code for converting thermal images to blood flow can be found under [main](https://github.com/SvrAdityaReddy/Thermography_based_Blood_Flow_Imaging/tree/master/main) directory as [thermal_blood_flow.ipynb](https://github.com/SvrAdityaReddy/Thermography_based_Blood_Flow_Imaging/blob/master/main/thermal_blood_flow.ipynb)

# References

[1] [Sagaidachnyi, A. A., et al. "Thermography-based blood flow imaging in human skin of the hands and feet: a spectral filtering approach." Physiological measurement 38.2 (2017): 272.](http://iopscience.iop.org/article/10.1088/1361-6579/aa4eaf/meta)
