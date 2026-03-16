from __future__ import annotations

import re


def _collapse_spaces(text: str) -> str:
    return ' '.join(text.split())


def canonicalize_intervention(value: str | None) -> str | None:
    if value is None:
        return None
    text = _collapse_spaces(value.lower())

    intervention_aliases = {
        'sodium butyrate supplementation': 'sodium butyrate',
        'sodium butyrate supplement': 'sodium butyrate',
        'oral sodium butyrate': 'sodium butyrate',
        'sodium butyrate administration': 'sodium butyrate',
        'oral butyrate': 'butyrate',
        'butyrate administration': 'butyrate',
        'butyrate supplementation': 'butyrate',
        'high-butyrate donor fecal transfer': 'high-butyrate donor fecal transfer',
        'dasatinib + quercetin': 'dasatinib plus quercetin',
        'intermittent dasatinib plus quercetin treatment': 'dasatinib plus quercetin',
        'weekly dasatinib plus quercetin treatment': 'dasatinib plus quercetin',
        'oral dasatinib plus quercetin treatment': 'dasatinib plus quercetin',
        'senolytic treatment (fisetin or dasatinib plus quercetin)': 'mixed senolytic treatment',
        'intermittent fisetin supplementation': 'fisetin',
        'oral fisetin treatment': 'fisetin',
        'fisetin administration': 'fisetin',
        'navitoclax (abt-263) treatment': 'navitoclax',
    }
    if text in intervention_aliases:
        return intervention_aliases[text]

    if 'sodium butyrate' in text:
        return 'sodium butyrate'
    if re.fullmatch(r'(oral )?butyrate( administration| supplementation)?', text):
        return 'butyrate'
    return text


def canonicalize_outcome(value: str | None) -> str | None:
    if value is None:
        return None
    text = _collapse_spaces(value.lower())
    text = text.replace('aβ', 'amyloid-beta ')
    text = text.replace('β', 'beta')
    text = text.replace('nf-kb', 'nf-κb')

    exact_aliases = {
        'neuroinflammatory response': 'neuroinflammation',
        'microglia-mediated neuroinflammation': 'neuroinflammation',
        'blood-brain barrier integrity': 'blood-brain barrier integrity',
        'bbb integrity': 'blood-brain barrier integrity',
        'aβ42 uptake and accumulation in endothelial cells': 'amyloid-beta uptake and accumulation',
        'amyloid-beta uptake and accumulation in endothelial cells': 'amyloid-beta uptake and accumulation',
        'amyloid-β uptake and accumulation in endothelial cells': 'amyloid-beta uptake and accumulation',
        'amyloid-beta pathology': 'amyloid-beta pathology',
        'memory deficits': 'memory deficits',
        'motor performance': 'motor performance',
        'cecal butyrate': 'cecal butyrate',
    }
    if text in exact_aliases:
        return exact_aliases[text]

    if 'neuroinflamm' in text:
        return 'neuroinflammation'
    if 'blood-brain barrier' in text or text.startswith('bbb '):
        return 'blood-brain barrier integrity'
    if 'amyloid' in text and 'uptake' in text and 'accumulation' in text:
        return 'amyloid-beta uptake and accumulation'
    if 'amyloid' in text and 'patholog' in text:
        return 'amyloid-beta pathology'
    return text


def canonicalize_mechanism_tag(value: str | None) -> str | None:
    if value is None:
        return None
    text = _collapse_spaces(value.lower())
    text = text.replace('nf-kb', 'nf-κb')

    exact_aliases = {
        'microbiome-gut-brain axis repair': 'microbiome-gut-brain axis',
        'gut-brain axis repair': 'microbiome-gut-brain axis',
        'tlr4/myd88/nf-κb pathway suppression': 'tlr4/myd88/nf-κb pathway inhibition',
        'tlr4/myd88/nf-κb pathway': 'tlr4/myd88/nf-κb pathway inhibition',
        'tlr4/myd88/nf-kb pathway suppression': 'tlr4/myd88/nf-κb pathway inhibition',
        'p-glycoprotein efflux transporter expression': 'p-glycoprotein efflux transporter',
        'scfa production': 'scfa production',
    }
    if text in exact_aliases:
        return exact_aliases[text]

    if 'tlr4' in text and 'myd88' in text and ('nf-κb' in text or 'nf-kb' in text):
        return 'tlr4/myd88/nf-κb pathway inhibition'
    if 'microbiome' in text and 'gut-brain axis' in text:
        return 'microbiome-gut-brain axis'
    if 'p-glycoprotein' in text:
        return 'p-glycoprotein efflux transporter'
    return text
