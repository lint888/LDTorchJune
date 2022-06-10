label_dict = {"(2 + 1)-dimensional non-linear optical waves through the coherently excited resonant medium doped with the erbium atoms can be described by a (2 + 1)-dimensional non-linear Schrodinger equation coupled with the self-induced transparency equations. For such a system, via the Hirota method and symbolic computation, linear forms, one-, two-and N-soliton solutions are obtained. Asymptotic analysis is conducted and suggests that the interaction between the two solitons is elastic. Bright solitons are obtained for the fields E and P, while the dark ones for the field N, with E as the electric field, P as the polarization in the resonant medium induced by the electric field, and N as the population inversion profile of the dopant atoms. Head-on interaction between the bidirectional two solitons and overtaking interaction between the unidirectional two solitons are seen. Influence of the averaged natural frequency. on the solitons are studied: (1). can affect the velocities of all the solitons; (2) Amplitudes of the solitons for the fields P and N increase with. decreasing, and decrease with. increasing; (3) With. decreasing, for the fields P and N, one-peak one soliton turns into the two-peak one, as well as interaction type changes from the interaction between two one-peak ones to that between a one-peak one and a two-peak one; (4) For the field E, influence of. on the solitons cannot be found. The results of this paper might be of potential applications in the design of optical communication systems which can produce the bright and dark solitons simultaneously." : 12,"(beta-amyloid (A beta) and tau pathology become increasingly prevalent with age, however, the spatial relationship between the two pathologies remains unknown. We examined local (same region) and non-local (different region) associations between these 2 aggregated proteins in 46 normal older adults using [F-18]AV-1451 (for tau) and [C-11]PiB (for A beta) positron emission tomography (PET) and 1.5 T magnetic resonance imaging (MRI) images. While local voxelwise analyses showed associations between PiB and AV-1451 tracer largely in the temporal lobes, k-means clustering revealed that some of these associations were driven by regions with low tracer retention. We followed this up with a whole-brain region-by-region (local and non-local) partial correlational analysis. We calculated each participant's mean AV-1451 and PiB uptake values within 87 regions of interest (ROI). Pairwise ROI analysis demonstrated many positive PiB AV-1451 associations. Importantly, strong positive partial correlations (controlling for age, sex, and global gray matter fraction, p <.01) were identified between PiB in multiple regions of association cortex and AV-1451 in temporal cortical ROIs. There were also less frequent and weaker positive associations of regional PiB with frontoparietal AV-1451 uptake. Particularly in temporal lobe ROIs, AV-1451 uptake was strongly predicted by NB across multiple ROI locations. These data indicate that A beta and tau pathology show significant local and non-local regional associations among cognitively normal elderly, with increased PiB uptake throughout the cortex correlating with increased temporal lobe AV-1451 uptake. The spatial relationship between A beta and tau accumulation does not appear to be specific to A beta location, suggesting a regional vulnerability of temporal brain regions to tau accumulation regardless of where AP accumulates.":2}
print(label_dict)
import Cla


from transformers import AutoModel, AutoTokenizer

MODEL_NAME_OR_PATH = "allenai/longformer-base-4096"

tokenizer = AutoTokenizer.from_pretrained(
    'allenai/longformer-base-4096'
)

model = AutoModel.from_pretrained(
    'allenai/longformer-base-4096'
)
text = "(2 + 1)-dimensional non-linear optical waves through the coherently excited resonant medium doped with the erbium atoms can be described by a (2 + 1)-dimensional non-linear Schrodinger equation coupled with the self-induced transparency equations. For such a system, via the Hirota method and symbolic computation, linear forms, one-, two-and N-soliton solutions are obtained. Asymptotic analysis is conducted and suggests that the interaction between the two solitons is elastic. Bright solitons are obtained for the fields E and P, while the dark ones for the field N, with E as the electric field, P as the polarization in the resonant medium induced by the electric field, and N as the population inversion profile of the dopant atoms. Head-on interaction between the bidirectional two solitons and overtaking interaction between the unidirectional two solitons are seen. Influence of the averaged natural frequency. on the solitons are studied: (1). can affect the velocities of all the solitons; (2) Amplitudes of the solitons for the fields P and N increase with. decreasing, and decrease with. increasing; (3) With. decreasing, for the fields P and N, one-peak one soliton turns into the two-peak one, as well as interaction type changes from the interaction between two one-peak ones to that between a one-peak one and a two-peak one; (4) For the field E, influence of. on the solitons cannot be found. The results of this paper might be of potential applications in the design of optical communication systems which can produce the bright and dark solitons simultaneously."#"Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
print(output['pooler_output'].shape)


model1 = Cla.Net()
print(model1.forward(output['pooler_output']))