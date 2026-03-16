# Science Compiler Report

## Summary

- Raw claims: 16
- Curated claims: 16
- Contradictions: 0
- Mechanism families: 15
- Experiment proposals: 0

## Claims

- pmid_29988130::C1 | dasatinib plus quercetin -> physical function and lifespan | effect=increase | source=pmid_29988130 | evidence_weight=5.50
  - summary: Intermittent senolytic treatment with dasatinib plus quercetin improves physical function and increases lifespan in old mice.
  - mechanism tags: senescent cell clearance
  - context: species=mouse, model_system=naturally aged and senescent cell-transplanted, administration_route=oral, time_horizon=late-life intervention
- pmid_30279143::C1 | fisetin -> lifespan extension | effect=increase | source=pmid_30279143 | evidence_weight=5.60
  - summary: Fisetin extends both median and maximum lifespan in progeroid and naturally aged mice when administered late in life.
  - mechanism tags: senescence reduction, senolytic activity
  - context: species=mouse, model_system=progeroid and naturally aged, administration_route=oral, time_horizon=late in life
- pmid_30279143::C2 | fisetin -> senescence marker reduction | effect=decrease | source=pmid_30279143 | evidence_weight=5.70
  - summary: Fisetin reduces senescence markers across multiple tissues and lowers SASP factors such as IL-6 and TNF-alpha in aged mice.
  - mechanism tags: sasp suppression, senolytic activity
  - context: species=mouse, model_system=progeroid and naturally aged, tissue=multiple tissues, administration_route=oral, time_horizon=late in life
- pmid_32509782::C1 | navitoclax -> trabecular bone volume fraction | effect=decrease | source=pmid_32509782 | evidence_weight=5.40
  - summary: Navitoclax treatment causes rapid trabecular bone loss in aged mice.
  - mechanism tags: senescent cell clearance
  - context: species=mouse, tissue=trabecular bone, disease_state=aged
- pmid_32509782::C2 | navitoclax -> osteoprogenitor and osteoblast function | effect=decrease | source=pmid_32509782 | evidence_weight=5.50
  - summary: Navitoclax strongly impairs osteoprogenitor and osteoblast function, causing cytotoxicity, apoptosis, and failure of mineralized matrix production.
  - mechanism tags: apoptosis, cytotoxicity
  - context: species=mouse, tissue=bone, disease_state=aged
- pmid_33832488::C1 | dasatinib plus quercetin -> liver disease progression | effect=increase | source=pmid_33832488 | evidence_weight=4.40
  - summary: The senolytic cocktail dasatinib plus quercetin mildly exacerbated obesity- and age-dependent liver disease progression and tumorigenesis in mice.
  - mechanism tags: senolytic therapy
  - context: species=mouse, disease_state=obesity- and age-dependent nafld/hcc, administration_route=oral
- pmid_34103349::C1 | mixed senolytic treatment -> coronavirus-related mortality in old mice | effect=decrease | source=pmid_34103349 | evidence_weight=5.60
  - summary: Senolytic interventions significantly reduced mortality in old mice exposed to a SARS-CoV-2-related mouse coronavirus.
  - mechanism tags: reduced inflammatory amplification, senescent cell clearance
  - context: species=mouse, model_system=old mice, disease_state=coronavirus infection, administration_route=oral
- pmid_34480023::C1 | dasatinib plus quercetin -> age-dependent intervertebral disc degeneration | effect=decrease | source=pmid_34480023 | evidence_weight=5.70
  - summary: Long-term weekly dasatinib plus quercetin treatment ameliorates age-dependent intervertebral disc degeneration in mice, with earlier or mid-life intervention being more effective than very late treatment.
  - mechanism tags: reduction of sasp molecules, reduction of senescence markers, senolytic activity
  - context: species=mouse, disease_state=age-dependent intervertebral disc degeneration, administration_route=weekly treatment, time_horizon=long-term
- pmid_35869934::C1 | dasatinib plus quercetin -> hepatocellular carcinoma incidence | effect=decrease | source=pmid_35869934 | evidence_weight=5.70
  - summary: Senolytic treatment with dasatinib plus quercetin sharply reduced hepatocellular carcinoma incidence in Sod1 knockout mice.
  - mechanism tags: inflammation reduction, senescence reduction
  - context: species=mouse, model_system=sod1 knockout, tissue=liver, disease_state=accelerated aging, administration_route=oral
- pmid_35869934::C2 | dasatinib plus quercetin -> liver senescence and necroptosis | effect=decrease | source=pmid_35869934 | evidence_weight=5.70
  - summary: Senolytic treatment reduced senescence markers, SASP factors, inflammation, and necroptosis in the liver of Sod1 knockout mice.
  - mechanism tags: inflammation reduction, senolytic activity
  - context: species=mouse, model_system=sod1 knockout, tissue=liver, disease_state=accelerated aging, administration_route=oral
- pmid_37296266::C1 | fisetin -> metabolism and cognition | effect=conditional | source=pmid_37296266 | evidence_weight=4.50
  - summary: Monthly oral fisetin treatment improved metabolism and cognition in male mice but had negligible effects in females.
  - mechanism tags: senolytic
  - context: species=mouse, model_system=c57bl/6, administration_route=oral, time_horizon=monthly treatment, notes=sex-specific effects
- pmid_37296266::C2 | dasatinib plus quercetin -> metabolism and cognition | effect=conditional | source=pmid_37296266 | evidence_weight=4.50
  - summary: Monthly oral dasatinib plus quercetin treatment had minimal effects in male mice but was detrimental in females, increasing adiposity, elevating SASP-related markers, reducing energy metabolism, and worsening object-recognition memory.
  - mechanism tags: senolytic
  - context: species=mouse, model_system=c57bl/6, administration_route=oral, time_horizon=monthly treatment, notes=sex-specific effects
- pmid_37396956::C1 | dasatinib plus quercetin -> overall influenza responses | effect=null | source=pmid_37396956 | evidence_weight=5.20
  - summary: Senolytic treatment with dasatinib and quercetin does not improve overall influenza responses in aged mice.
  - context: species=mouse, disease_state=influenza infection, notes=aged mice
- pmid_37396956::C2 | dasatinib plus quercetin -> flu-specific cd8 t-cell infiltration | effect=decrease | source=pmid_37396956 | evidence_weight=5.50
  - summary: Dasatinib plus quercetin causes a transient decrease in flu-specific CD8 T-cell infiltration during primary infection in aged mice.
  - mechanism tags: immune cell infiltration
  - context: species=mouse, tissue=lung, disease_state=influenza infection, time_horizon=transient, notes=aged mice, primary infection
- pmid_38062873::C1 | fisetin -> arterial function | effect=increase | source=pmid_38062873 | evidence_weight=5.70
  - summary: Intermittent fisetin supplementation improves arterial function in old mice.
  - mechanism tags: cellular senescence reduction, senolytic
  - context: species=mouse, tissue=vascular, disease_state=aging, administration_route=oral, time_horizon=intermittent
- pmid_38062873::C2 | fisetin -> cellular senescence | effect=decrease | source=pmid_38062873 | evidence_weight=5.70
  - summary: Fisetin decreases cellular senescence markers and SASP-associated inflammation in old mice.
  - mechanism tags: inflammation reduction, senolytic
  - context: species=mouse, tissue=vascular, disease_state=aging, administration_route=oral, time_horizon=intermittent

## Ranked Claims

- score=38 | evidence_weight=4.50 | tier=headline | pmid_37296266::C1 | fisetin -> metabolism and cognition
- score=38 | evidence_weight=4.50 | tier=headline | pmid_37296266::C2 | dasatinib plus quercetin -> metabolism and cognition
- score=24 | evidence_weight=5.50 | tier=supporting | pmid_29988130::C1 | dasatinib plus quercetin -> physical function and lifespan
- score=24 | evidence_weight=5.60 | tier=supporting | pmid_30279143::C1 | fisetin -> lifespan extension
- score=24 | evidence_weight=5.70 | tier=supporting | pmid_30279143::C2 | fisetin -> senescence marker reduction
- score=24 | evidence_weight=5.60 | tier=supporting | pmid_34103349::C1 | mixed senolytic treatment -> coronavirus-related mortality in old mice
- score=24 | evidence_weight=5.70 | tier=supporting | pmid_34480023::C1 | dasatinib plus quercetin -> age-dependent intervertebral disc degeneration
- score=24 | evidence_weight=5.70 | tier=supporting | pmid_35869934::C1 | dasatinib plus quercetin -> hepatocellular carcinoma incidence
- score=24 | evidence_weight=5.70 | tier=supporting | pmid_35869934::C2 | dasatinib plus quercetin -> liver senescence and necroptosis
- score=24 | evidence_weight=5.50 | tier=supporting | pmid_37396956::C2 | dasatinib plus quercetin -> flu-specific cd8 t-cell infiltration
- score=24 | evidence_weight=5.70 | tier=supporting | pmid_38062873::C1 | fisetin -> arterial function
- score=24 | evidence_weight=5.70 | tier=supporting | pmid_38062873::C2 | fisetin -> cellular senescence
- score=23 | evidence_weight=5.40 | tier=supporting | pmid_32509782::C1 | navitoclax -> trabecular bone volume fraction
- score=23 | evidence_weight=5.50 | tier=supporting | pmid_32509782::C2 | navitoclax -> osteoprogenitor and osteoblast function
- score=22 | evidence_weight=4.40 | tier=supporting | pmid_33832488::C1 | dasatinib plus quercetin -> liver disease progression
- score=22 | evidence_weight=5.20 | tier=supporting | pmid_37396956::C1 | dasatinib plus quercetin -> overall influenza responses

## Evidence Balance

- dasatinib plus quercetin -> age-dependent intervertebral disc degeneration | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- dasatinib plus quercetin -> flu-specific cd8 t-cell infiltration | leading_effect=decrease | net_support=5.50 | claims=1
  - weighted support: decrease=5.50
- dasatinib plus quercetin -> hepatocellular carcinoma incidence | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- dasatinib plus quercetin -> liver disease progression | leading_effect=increase | net_support=-4.40 | claims=1
  - weighted support: increase=4.40
- dasatinib plus quercetin -> liver senescence and necroptosis | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- dasatinib plus quercetin -> metabolism and cognition | leading_effect=conditional | net_support=0.00 | claims=1
  - weighted support: conditional=4.50
- dasatinib plus quercetin -> overall influenza responses | leading_effect=null | net_support=0.00 | claims=1
  - weighted support: null=5.20
- dasatinib plus quercetin -> physical function and lifespan | leading_effect=increase | net_support=-5.50 | claims=1
  - weighted support: increase=5.50
- fisetin -> arterial function | leading_effect=increase | net_support=-5.70 | claims=1
  - weighted support: increase=5.70
- fisetin -> cellular senescence | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- fisetin -> lifespan extension | leading_effect=increase | net_support=-5.60 | claims=1
  - weighted support: increase=5.60
- fisetin -> metabolism and cognition | leading_effect=conditional | net_support=0.00 | claims=1
  - weighted support: conditional=4.50
- fisetin -> senescence marker reduction | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- mixed senolytic treatment -> coronavirus-related mortality in old mice | leading_effect=decrease | net_support=5.60 | claims=1
  - weighted support: decrease=5.60
- navitoclax -> osteoprogenitor and osteoblast function | leading_effect=decrease | net_support=5.50 | claims=1
  - weighted support: decrease=5.50
- navitoclax -> trabecular bone volume fraction | leading_effect=decrease | net_support=5.40 | claims=1
  - weighted support: decrease=5.40

## Family-Split Evidence Balance

- intervention_family=other | disease_family=aging | outcome=arterial function | leading_effect=increase | net_support=-5.70 | claims=1
  - weighted support: increase=5.70
- intervention_family=other | disease_family=aging | outcome=cellular senescence | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- intervention_family=other | disease_family=aging | outcome=hepatocellular carcinoma incidence | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- intervention_family=other | disease_family=aging | outcome=lifespan extension | leading_effect=increase | net_support=-5.60 | claims=1
  - weighted support: increase=5.60
- intervention_family=other | disease_family=aging | outcome=liver senescence and necroptosis | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- intervention_family=other | disease_family=aging | outcome=osteoprogenitor and osteoblast function | leading_effect=decrease | net_support=5.50 | claims=1
  - weighted support: decrease=5.50
- intervention_family=other | disease_family=aging | outcome=physical function and lifespan | leading_effect=increase | net_support=-5.50 | claims=1
  - weighted support: increase=5.50
- intervention_family=other | disease_family=aging | outcome=senescence marker reduction | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- intervention_family=other | disease_family=aging | outcome=trabecular bone volume fraction | leading_effect=decrease | net_support=5.40 | claims=1
  - weighted support: decrease=5.40
- intervention_family=other | disease_family=metabolic_inflammation | outcome=liver disease progression | leading_effect=increase | net_support=-4.40 | claims=1
  - weighted support: increase=4.40
- intervention_family=other | disease_family=other | outcome=age-dependent intervertebral disc degeneration | leading_effect=decrease | net_support=5.70 | claims=1
  - weighted support: decrease=5.70
- intervention_family=other | disease_family=other | outcome=coronavirus-related mortality in old mice | leading_effect=decrease | net_support=5.60 | claims=1
  - weighted support: decrease=5.60
- intervention_family=other | disease_family=other | outcome=flu-specific cd8 t-cell infiltration | leading_effect=decrease | net_support=5.50 | claims=1
  - weighted support: decrease=5.50
- intervention_family=other | disease_family=other | outcome=metabolism and cognition | leading_effect=conditional | net_support=0.00 | claims=2
  - weighted support: conditional=9.00
- intervention_family=other | disease_family=other | outcome=overall influenza responses | leading_effect=null | net_support=0.00 | claims=1
  - weighted support: null=5.20

## Contradictions

- None

## Mechanism Families

- senolytic | evidence_count=4
  - claims: pmid_37296266::C1, pmid_37296266::C2, pmid_38062873::C1, pmid_38062873::C2
  - intervention/outcomes: dasatinib plus quercetin -> metabolism and cognition, fisetin -> arterial function, fisetin -> cellular senescence, fisetin -> metabolism and cognition
- senolytic activity | evidence_count=4
  - claims: pmid_30279143::C1, pmid_30279143::C2, pmid_34480023::C1, pmid_35869934::C2
  - intervention/outcomes: dasatinib plus quercetin -> age-dependent intervertebral disc degeneration, dasatinib plus quercetin -> liver senescence and necroptosis, fisetin -> lifespan extension, fisetin -> senescence marker reduction
- inflammation reduction | evidence_count=3
  - claims: pmid_35869934::C1, pmid_35869934::C2, pmid_38062873::C2
  - intervention/outcomes: dasatinib plus quercetin -> hepatocellular carcinoma incidence, dasatinib plus quercetin -> liver senescence and necroptosis, fisetin -> cellular senescence
- senescent cell clearance | evidence_count=3
  - claims: pmid_29988130::C1, pmid_32509782::C1, pmid_34103349::C1
  - intervention/outcomes: dasatinib plus quercetin -> physical function and lifespan, mixed senolytic treatment -> coronavirus-related mortality in old mice, navitoclax -> trabecular bone volume fraction
- senescence reduction | evidence_count=2
  - claims: pmid_30279143::C1, pmid_35869934::C1
  - intervention/outcomes: dasatinib plus quercetin -> hepatocellular carcinoma incidence, fisetin -> lifespan extension
- apoptosis | evidence_count=1
  - claims: pmid_32509782::C2
  - intervention/outcomes: navitoclax -> osteoprogenitor and osteoblast function
- cellular senescence reduction | evidence_count=1
  - claims: pmid_38062873::C1
  - intervention/outcomes: fisetin -> arterial function
- cytotoxicity | evidence_count=1
  - claims: pmid_32509782::C2
  - intervention/outcomes: navitoclax -> osteoprogenitor and osteoblast function
- immune cell infiltration | evidence_count=1
  - claims: pmid_37396956::C2
  - intervention/outcomes: dasatinib plus quercetin -> flu-specific cd8 t-cell infiltration
- reduced inflammatory amplification | evidence_count=1
  - claims: pmid_34103349::C1
  - intervention/outcomes: mixed senolytic treatment -> coronavirus-related mortality in old mice
- reduction of sasp molecules | evidence_count=1
  - claims: pmid_34480023::C1
  - intervention/outcomes: dasatinib plus quercetin -> age-dependent intervertebral disc degeneration
- reduction of senescence markers | evidence_count=1
  - claims: pmid_34480023::C1
  - intervention/outcomes: dasatinib plus quercetin -> age-dependent intervertebral disc degeneration
- sasp suppression | evidence_count=1
  - claims: pmid_30279143::C2
  - intervention/outcomes: fisetin -> senescence marker reduction
- senolytic therapy | evidence_count=1
  - claims: pmid_33832488::C1
  - intervention/outcomes: dasatinib plus quercetin -> liver disease progression
- unspecified mechanism | evidence_count=1
  - claims: pmid_37396956::C1
  - intervention/outcomes: dasatinib plus quercetin -> overall influenza responses

## Experiment Proposals
