# Restoring Real-World Degraded Events Improves Deblurring Quality (ACMMM2024)

![fig1](https://github.com/user-attachments/assets/81688844-aa08-4e22-9b10-2ddeff0a31b6)

## Abstract
Due to its high speed and low latency, DVS is frequently employed in motion deblurring. Ideally, high-quality events would adeptly capture intricate motion information. However, real-world events are generally degraded, thereby introducing significant artifacts into the deblurred results. In response to this challenge, we model the degradation of events and propose RDNet to improve the quality of image deblurring. Specifically, we first analyze the mechanisms underlying degradation and simulate paired events based on that. These paired events are then fed into the first stage of the RDNet for training the restoration model. The events restored in this stage serve as a guide for the second-stage deblurring process. To better assess the deblurring performance of different methods on real-world degraded events, we present a new real-world dataset named DavisMCR. This dataset incorporates events with diverse degradation levels, collected by manipulating environmental brightness and target object contrast. Our experiments are conducted on synthetic datasets (GOPRO), real-world datasets (REBlur), and the proposed dataset (DavisMCR). The results demonstrate that RDNet outperforms classical event denoising methods in event restoration. Furthermore, RDNet exhibits better performance in deblurring tasks compared to state-of-the-art methods.

## Method
<img width="1014" alt="pipeline2" src="https://github.com/user-attachments/assets/9109deac-8fa6-4931-8dcd-0828a77d2844">
The event degradation process and the pipeline of RDNet. The red region (1) above illustrates the event degradation process for constructing paired data of undegraded $E_{u}$ and degraded events $E_{d}$. (a) illustrates how threshold bias introduces differences in events. (b) represents how limited bandwidth leads to event loss. (c) provides visualization of simulated circuit noise. The yellow region (2) below is the first-stage event restoration. Degraded events $E_{d}$ and blurry image $I_{b}$ are fed into dual-branch encoders, and a single-branch event decoder generates the restored event $E_{r}$. The ground-truth is undegraded event $E_{u}$, and the loss is $L_{er}$. The green region (3) below is the second-stage event-based deblurring. Restored event $E_{r}$ and blurry image $I_{b}$ are fed into dual-branch encoders, and a single-branch image decoder generates the deblurred image $I_{d}$. The ground-truth is sharp images $I_{s}$, and the loss is $L_{d}$.

## DavisMCR 

<img src="https://github.com/user-attachments/assets/432ec84e-3f0a-40a0-aed2-8d85c5689b43" alt="dataset_details" width="500">

The innovation of DavisMCR dataset. 
(a) represents the control group, capturing a normal contrast text motion scene under the illumination of lux=800. The events exhibit clear textures with minimal noise.
(b) depicts a low-contrast text motion scene, where events are relatively weak, and the edges are less defined.
(c) showcases a text motion scene captured in a high-lux environment, displaying events with clear edges and minimal noise.
(d) presents a text motion scene with a dark background, showing events with severe background noise.
(e) illustrates a natural scene with events containing diverse forms and various intensity levels.


<img src="https://github.com/user-attachments/assets/4147020e-a61f-4376-9900-7d27fbcd88ed" alt="dataset_all" width="700">

The columns display images and events captured under different ambient brightness conditions. Distinct ambient brightness levels are typically associated with varying signal-to-noise ratios. APS1 and APS2 represent bright and dark background brightness, respectively. DVS2 captured against a dark background exhibits more noise than DVS1. Objects in different rows within each image have different contrasts. The events in areas with strong contrast are dense and clear.

### Download
**Preprocessed subset dataset link:**  [Baidu(h0fr)](https://pan.baidu.com/s/1zTHZnG6a8AS3BaVpuBfJWw?pwd=h0fr) | [GoogleDrive](https://drive.google.com/drive/folders/1jkIK82pOCQO86lldKB9H1FK_XE8SOqPo?usp=drive_link)
  - [root] 
      - [lux300_40ms] (Lux=300, exposure time=40ms)
          - [scene1]
              - [img1.png]
              - [events1.bin] (Events corresponding to img1.png)
              - [event_vis1.png](Visualization of events1.bin)
            
**Complete dataset raw file link:**  [Baidu(h79b)](https://pan.baidu.com/s/1IdYlkIRGbpgg-FYZumBNug?pwd=h79b) | [GoogleDrive](https://drive.google.com/drive/folders/1id8DwF1_UmLZOZ8B56DJPg7V4JHL8I8A?usp=drive_link)
  - [root] 
      - [lux300_40ms] (Lux=300, exposure time=40ms)
          - dvSave-2023_11_08_15_37_18.aedat4
