# mBCI (RAISE 2020 Project)

Building an Arduino-Based Brain-Computer Interface and Writing a Real-Time Signal Plotting Program

## Introduction

With the recent progress of startups like Neuralink and Neurable, *brain-computer interfaces* are emerging as ‘the next big thing’ in the consumer tech market. A brain-computer interface or BCI is a device that can read and interpret neural signals, such as electroencephalography (EEG). BCIs are interdisciplinary, combining neuroscience, circuits, signal processing and machine learning, and their immense complexity often requires a team of experts to create a novel system. This project aimed to understand basic neuroscience and circuit concepts and resulted in creating an Arduino-based BCI and a real-time signal plotting program (mBCI Lab). Specifically, an Arduino Duemila and an EEG circuit design from an existing BCI project were used to create the BCI circuit, and the real-time signal plotting program was based upon a Python-based, real-time graphing project by Sepúlvelda et al. in 2014. 



## In This Repository

### Overview of Directories and Folders in this Repository

- arduino – contains the Arduino code used to drive the BCI
- datasheets – contains the datasheets for the amplifiers (instrument & operational) used to create the BCI's amplification/filter module
- guis – contains mBCI Lab v0.0.1 + prototype GUIs
- misc – contains miscallenous code examples + Flicker Lab (a variable-FPS checkerboard pattern flicker program)
- papers – contains papers/articles/links used to create the BCI
- photos – contains photos of BCI + mBCI Lab + circuit schematics



## RAISE Project Details

### Background

Brain-computer interfaces embody concepts from neuroscience, circuits, signal processing, and machine learning. Leveraging this technology allows [] to do [], [] to do [], and [] to do [].



### Approach

#### Schedule (and learning materials)

- Week 1: Learning the basics of neuroscience, BCI, and neural signals.
  - Neurobiology
  - 
- Week 2: Learning C/C++ syntax and setting up Arduino coding environment.
  - Codecademy C & C++ courses
  - Arduino Programming Language Reference
- Week 3: Learning the basics of circuits and building BCI circuit.
  - 
- Week 4: Building the real-time signal plotting software.
- Week 5: Finishing the real-time signal plotting software and testing the BCI circuit and signal acquisition software.

#### Existing BCI Projects



#### Building the circuit

##### existing bci projects

I referenced the following EEG projects to build the circuit:

I followed the schematic.

#### Building the software

first built prototype in python tkinter

then built a prototype in pyqt5

then found an open-source real-time plotter in pyqt5



### Results

#### A Minimal Brain-Computer Interface Circuit

**Figure 3. An image of a minimal BCI circuit.** The circuit uses an Arduino Duemila (boxed in cyan) and connects to a computer via a micro-USB to USB cable (not pictured). The electrodes (circled in orange) connect to the locations on the scalp associated with the desired neural signal, and the amplification/filter module (boxed in light purple) amplifies and filters the neural signal. Amplification increase the strength of the signal, and filtering removes the unwanted noise in the signal. This BCI circuit is minimal in the sense that it reads neural signal from a single location and utilizes a relatively basic amplification/filter module. The amplification/filter module is a wiring of []'s module schematic (citation).

#### The Software

**Figure 4. A screenshot of** **mBCI** **Lab.** mBCI Lab is based on Sepúlvelda et al.’s RTGraph project, a real-time signal plotting program written in Python. Specifically, mBCI Lab utilizes the backend processing of RTGraph and introduces a new graphical user interface for interacting with the mBCI. The former is written as a fork (or copy) of the latter. *The signal present in this screenshot is random noise from a BCI that is not connected to a subject.

### Discussion

things that went well

- learned about bci, neurons, circuits
  - bci's are devices...
  - neurons are cells...
  - circuits are wires...

### Next Steps

1. Refine understanding of circuits and learn more advanced circuit topics - This project was mainly focused on exploring the fundamentals of each discipline involved in brain-computer interfaces.

2. Data Collection - This minimal brain-computer interface can be used to collect single-channel EEG data. 

3. Neural Signal Analysis - Once neural signal has been collected, the BCI 

4. Machine Learning - Machine learning can be leveraged to callibrate different types of neural signals to actionable tasks (e.g. move cursur up/down and left/right on a screen), which could make the BCI useful as an input or control device for a computer or phone.




### References

1. Sepúlveda S, Reyes P, and Weinstein A. Visualizing physiological signals in real-time. *Proc.* of the 14th *Python in Science Conf.,* 182-186 (2015).
2. cornell eeg
3. eeg home project
4. 



### Acknowledgements

I'd like to thank Professor Osborn (Pomona College Computer Science) for his mentorship and the Fletcher Jones Foundation for funding my summer project.