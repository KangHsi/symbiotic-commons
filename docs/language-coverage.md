# Language reach: target, evidence, and limits

## Status

The requested ambition is to make a complete whitepaper understandable to **at least 90% of people worldwide**. This release does **not** certify that threshold. Edition count, country count, internet-user share, and the sum of first- and second-language speakers are different quantities.

The launch set is an editorial selection of widely used and regionally important written languages, with separate Chinese script editions. It is not a statistically certified 90% set. No language is included as evidence that every speaker of a related variety can read it. Drafts need fluent review; availability is not proof of comprehension.

## Why simple addition fails

A bilingual reader appears in the speaker totals of two languages. Official language status does not imply that everyone in a country reads that language. Script familiarity, regional variety, age, literacy, disability, internet access, and translation quality also affect real access.

Unicode's [CLDR territory-language documentation](https://www.unicode.org/cldr/charts/48/supplemental/territory_language_information.html) explicitly describes overlapping language populations and estimates from mixed sources. Its [population-data guidance](https://cldr.unicode.org/index/requesting-additionsupdates-to-cldr-languagepopulation-data) explains the locale-selection purpose and source requirements. [UNESCO's multilingualism overview](https://www.unesco.org/en/multilingualism-linguistic-diversity) supplies broader context for linguistic and digital inclusion.

## A reproducible conservative method—and its limitation

For each territory, let p(l,t) be the reported share using an available language l. Without joint-language information:

- Lower bound on the union: max p(l,t).
- Upper bound: min(1, sum p(l,t)).
- Weight each territory by a consistent population denominator.

The lower bound does not add overlapping speakers. It is often very loose in multilingual territories; it is not a best estimate of actual reach.

An exploratory calculation using official [CLDR JSON release 48.0.0](https://github.com/unicode-org/cldr-json/blob/48.0.0/cldr-json/cldr-core/supplemental/territoryInfo.json), with its own territory populations and populationPercent values, produced a lower bound of approximately **74.16% even when every listed language was allowed**. This demonstrates why this method cannot certify a 90% threshold. It does not mean this release reaches 74.16%, nor that actual global reach cannot exceed that number. The input populations use mixed dates and do not form a new global census.

## Work needed to substantiate the target

1. Define the denominator and the criterion: for example, reading and understanding at least one complete edition. Literal all-population access also requires age-appropriate, audio, and other accessible formats.
2. Select a reference year and assemble territory-level census or survey observations on comprehension and literacy.
3. Use joint-language data or valid non-overlapping groups, and account for missing territories and uncertainty.
4. Map observations to the actual published written standards and scripts; do not substitute a macrolanguage or official language label without evidence.
5. Verify translation quality and report availability separately from observed readership or comprehension.
6. Publish inputs, methods, uncertainty, and independent review. Claim a modeled estimate only as a modeled estimate; state achieved ≥90% only when evidence supports it.

The unresolved coverage requirement remains visible in [open questions](open-questions.md). Adding more editions can improve inclusion, but cannot replace this evidence.

## 中文说明

目标是让全球至少 90% 的人能够理解完整白皮书。本版尚不能验证这一比例。双语人口会重复计数，官方语言不等于所有居民都能阅读，简体与繁体版本也不是两个独立语言人口。

我们公开译文、来源版本和审阅状态，同时保留“90% 尚未验证”的说明。后续应结合语言重叠、识字率、文字系统和实际译文质量，建立可检查的覆盖评估。不同年龄、障碍和离线条件的读者还需要其他可及形式。
