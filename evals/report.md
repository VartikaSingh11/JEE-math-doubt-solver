# Evaluation Report

Golden set: 49 questions (48 answerable, 1 unanswerable)

- Retrieval hit-rate (top-3): **62%**
- Avg faithfulness (keyword): **73%**
- Refusal accuracy: **100%**

---

## Q1: For a quadratic equation ax^2 + bx + c = 0, what are the sum and product of its roots?

**Type:** recall | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['-b/a', 'c/a']

**Answer given:**
> The sum of the roots is -b/a and the product of the roots is c/a. (Source: Quadratic_Equations, Page 2)

**Chunks actually retrieved:**
- Quadratic_Equations, page 2 (score 0.658)
- Quadratic_Equations, page 1 (score 0.56)
- Quadratic_Equations, page 4 (score 0.483)

---

## Q2: Why do irrational roots of a quadratic equation with rational coefficients always occur in conjugate pairs?

**Type:** conceptual | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['conjugate', 'rational coefficient']

**Answer given:**
> Irrational roots of a quadratic equation with rational coefficients always occur in conjugate pairs because if one of the roots is m + √n, then the other root will be m - √n (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 2 (score 0.633)
- Quadratic_Equations, page 1 (score 0.604)
- Quadratic_Equations, page 12 (score 0.422)

---

## Q3: What are the three basic trigonometric identities relating sin, cos, tan, cot, sec, and cosec?

**Type:** recall | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 67% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3]
**Expected facts:** ['cos²', 'sec²', 'cosec²']

**Answer given:**
> The three basic trigonometric identities are: (1) sin²θ + cos²θ = 1, (2) tan²θ + 1 = sec²θ, and no third identity is explicitly listed as basic, but examples of other identities are provided (Source: Trigonometric_Ratios_and_Identities, Page 3).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 3 (score 0.617)
- Trigonometric_Ratios_and_Identities, page 19 (score 0.617)
- Trigonometric_Ratios_and_Identities, page 4 (score 0.61)

---

## Q4: If D is the discriminant of a quadratic equation, what does D > 0, D = 0, and D < 0 tell us about the nature of its roots?

**Type:** applied | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['real and distinct', 'coincident', 'no real']

**Answer given:**
> The discriminant D of a quadratic equation tells us that if D > 0, the roots are real and distinct, if D = 0, the roots are coincident, and if D < 0, there are no real roots (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 2 (score 0.625)
- Quadratic_Equations, page 1 (score 0.494)
- Quadratic_Equations, page 10 (score 0.487)

---

## Q5: Explain how to find the derivative of sin(x) using first principles.

**Type:** should_refuse | **Difficulty:** easy | **Retrieval:** n/a (unanswerable) | **Faithfulness:** n/a | **Refused:** True

**Expected:** should refuse (unanswerable question)

**Answer given:**
> This isn't covered in the provided material. 

The context provided focuses on trigonometric ratios and identities, but does not discuss derivatives or calculus (Source: Trigonometric_Ratios_and_Identities, Pages 12-17).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 13 (score 0.455)
- Trigonometric_Ratios_and_Identities, page 12 (score 0.347)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.339)

---

## Q6: Convert 225° into radians.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [2]
**Expected facts:** ['5π/4']

**Answer given:**
> The angle 225° is equal to 225 * (π/180) = 3.927 radians, or approximately 3.93 radians. (Source: Trigonometric_Ratios_and_Identities, Page 2)

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 2 (score 0.528)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.448)
- Trigonometric_Ratios_and_Identities, page 1 (score 0.433)

---

## Q7: Convert 7π/12 radians into degrees.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [2]
**Expected facts:** ['105']

**Answer given:**
> The angle 7π/12 radians is equivalent to 7π/12 * 180/π = 105° (Source: Trigonometric_Ratios_and_Identities, Page 2).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 2 (score 0.526)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.479)
- Trigonometric_Ratios_and_Identities, page 4 (score 0.455)

---

## Q8: Find the quadrant in which the angle –510° lies.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 50% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [1]
**Expected facts:** ['third quadrant', '210']

**Answer given:**
> The angle –510° lies in the III quadrant. 
Since the angle is measured from the positive x-axis in the anticlockwise direction and is negative, it will be measured in the clockwise direction, [Source: Trigonometric_Ratios_and_Identities, Page 1]. 
To find the equivalent positive angle, we add 360° to –510° until we get a positive angle between 0° and 360°. 
–510° + 2*360° = –510° + 720° = 210°. 
Since 180° < 210° < 270°, the angle lies in the III quadrant, [Source: Trigonometric_Ratios_and_Identities, Page 1].

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 1 (score 0.51)
- Trigonometric_Ratios_and_Identities, page 2 (score 0.489)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.48)

---

## Q9: If sin θ = 5/13 and θ is acute, find cos θ and tan θ.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3]
**Expected facts:** ['12/13', '5/12']

**Answer given:**
> The value of cos θ is 12/13 and tan θ is 5/12. 
Using the identity sin²θ + cos²θ = 1 (Source: Trigonometric_Ratios_and_Identities, Page 11), we can find cos θ: cos²θ = 1 - sin²θ = 1 - (5/13)² = 1 - 25/169 = 144/169, so cos θ = √(144/169) = 12/13. 
Then, tan θ = sin θ / cos θ = (5/13) / (12/13) = 5/12 (Source: Trigonometric_Ratios_and_Identities, Page 17).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 17 (score 0.453)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.437)
- Trigonometric_Ratios_and_Identities, page 11 (score 0.416)

---

## Q10: Prove that (1−cosθ)/(sinθ)=cosecθ−cotθ.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3, 4]
**Expected facts:** ['1/sinθ', 'cosθ/sinθ']

**Answer given:**
> The given expression (1−cosθ)/(sinθ) can be simplified to cosecθ−cotθ. 
We start with the left-hand side of the equation: (1−cosθ)/(sinθ). 
Using the identity sin²θ + cos²θ = 1 (Source: Trigonometric_Ratios_and_Identities, Page 3), we can rewrite 1 as sin²θ + cos²θ, giving us (sin²θ + cos²θ - cosθ)/(sinθ). 
This simplifies to (sin²θ - cosθ + cos²θ)/(sinθ), which can be further simplified to sin²θ/(sinθ) - cosθ/(sinθ) + cos²θ/(sinθ). 
Using the definitions of cosecθ = 1/sinθ and cotθ = cosθ/sinθ (Source: Trigonometric_Ratios_and_Identities, Page 3), we can rewrite this as sinθ - cosθ + cos²θ/(sinθ). 
Then, factoring out cosθ from the last two terms, we get sinθ - cosθ(1 - cosθ)/(sinθ), which simplifies to sinθ - cosθ(cosecθ - 1) (since 1 - cosθ = sin²θ/sin²θ * (1 - cosθ) = (1 - cos²θ)/sin²θ * sinθ = sinθ * (1 - cos²θ)/(sin²θ) = sinθ * (sin²θ)/(sin²θ) = sinθ, hence (1 - cosθ)/(sinθ) = cosecθ - 1, or 1 - cosθ = sinθ(cosecθ - 1)). 
However, a more direct approach is to use the definitions of cosecθ and cotθ directly on the initial expression (1−cosθ)/(sinθ) = (1/sinθ) - (cosθ/sinθ) = cosecθ - cotθ (Source: Trigonometric_Ratios_and_Identities, Page 4). 
Therefore, (1−cosθ)/(sinθ) = cosecθ − cotθ. (Source: Trigonometric_Ratios_and_Identities, Page 3 and Page 4).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 1 (score 0.43)
- Trigonometric_Ratios_and_Identities, page 3 (score 0.426)
- Trigonometric_Ratios_and_Identities, page 4 (score 0.399)

---

## Q11: Simplify sin(180°+θ)+cos(360°−θ).

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['cosθ − sinθ']

**Answer given:**
> The simplified expression is -sinθ + cosθ, since sin(180°+θ) = -sinθ (using the identity sin(A + B) = sinAcosB + cosAsinB, where sin180° = 0 and cos180° = -1) (Source: Trigonometric_Ratios_and_Identities, Page 12) and cos(360°−θ) = cosθ (using the identity cos(A - B) = cosAcosB + sinAsinB, where cos360° = 1 and sin360° = 0) (Source: Trigonometric_Ratios_and_Identities, Page 12).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 12 (score 0.544)
- Trigonometric_Ratios_and_Identities, page 13 (score 0.516)
- Trigonometric_Ratios_and_Identities, page 1 (score 0.48)

---

## Q12: Evaluate tan 255°.

**Type:** computational | **Difficulty:** hard | **Retrieval:** ❌ MISS | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7, 13]
**Expected facts:** ['2 + √3']

**Answer given:**
> The value of tan 255° is tan (255°) = tan (180° + 75°) = tan (180° - (-75°)) = tan (-75°) = -tan 75°, and since tan (90° - x) = cot x, we have tan 75° = tan (90° - 15°) = cot 15°, but we cannot find the exact value of cot 15° from the given context, so we need to use the identity tan (x) = -tan (360° - x) and the fact that tan (x) = tan (180° + x) to get tan 255° = -tan 75° = -tan (90° - 15°) = -cot 15°, and using the fact that cot x = 1/tan x, we have tan 255° = -1/tan 15°, and since tan 15° = 2 - sqrt(3) (Source: Trigonometric_Ratios_and_Identities, Page 18), we have tan 255° = -1/(2 - sqrt(3)) = -(2 + sqrt(3))/(2 - sqrt(3))(2 + sqrt(3)) = -(2 + sqrt(3))/1 = -2 - sqrt(3) ≈ -3.73 (Source: Trigonometric_Ratios_and_Identities, Page 18).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 18 (score 0.549)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.505)
- Trigonometric_Ratios_and_Identities, page 5 (score 0.497)

---

## Q13: Find sin75° using compound-angle formula.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [11, 12]
**Expected facts:** ['1+√3', '2√2']

**Answer given:**
> The value of sin75° is cos15°, which can be calculated using the compound-angle formula (Source: Trigonometric_Ratios_and_Identities, Page 12). 
To find cos15°, we can use the formula cos(A - B) = cosAcosB + sinAsinB, where A = 45° and B = 30° (Source: Trigonometric_Ratios_and_Identities, Page 12). 
Substituting the values, we get cos15° = cos(45° - 30°) = cos45°cos30° + sin45°sin30° = (√2/2)(√3/2) + (√2/2)(1/2) = (√6 + √2)/4. 
Therefore, sin75° = (√6 + √2)/4 ≈ 0.97.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 12 (score 0.598)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.538)
- Trigonometric_Ratios_and_Identities, page 13 (score 0.526)

---

## Q14: Express cos(2A) in terms of tanA.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [4, 15]
**Expected facts:** ['1 - tan²A', '1 + tan²A']

**Answer given:**
> The value of cos(2A) in terms of tanA is 1 - 2tan^2A / (1 + tan^2A) = (1 - tan^2A) / (1 + tan^2A), which simplifies to (1 - tan^2A) / (1 + tan^2A) = 1 - 2tan^2A / (1 + tan^2A) = (1 - tan^2A) / sec^2A = cos^2A - sin^2A = cos2A (Source: Trigonometric_Ratios_and_Identities, Page 4).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 4 (score 0.588)
- Trigonometric_Ratios_and_Identities, page 13 (score 0.575)
- Trigonometric_Ratios_and_Identities, page 16 (score 0.569)

---

## Q15: If secθ+tanθ=5, find secθ−tanθ.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3]
**Expected facts:** ['1/5']

**Answer given:**
> The value of secθ−tanθ is 1/5, since (secθ+tanθ)(secθ−tanθ) = sec²θ - tan²θ = 1 (Source: Trigonometric_Ratios_and_Identities, Page 17), and given secθ+tanθ = 5, we can rearrange to find secθ−tanθ = 1/(secθ+tanθ) = 1/5.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 17 (score 0.47)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.412)
- Trigonometric_Ratios_and_Identities, page 7 (score 0.389)

---

## Q16: Evaluate sin15° cos15°.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [12]
**Expected facts:** ['1/4']

**Answer given:**
> The value of sin15° cos15° is 1/4, since sin15° = cos75° and using the identity 2 sinA cosB = sin(A + B) + sin(A - B) (Source: Trigonometric_Ratios_and_Identities, Page 12), we can derive that 2 sin15° cos15° = sin(15° + 15°) + sin(15° - 15°) = sin30° + sin0° = 1/2 + 0 = 1/2, so sin15° cos15° = 1/4.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 12 (score 0.579)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.568)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.561)

---

## Q17: If tanθ=3/4 and θ is in III quadrant, find all trigonometric ratios.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3, 6]
**Expected facts:** ['-3/5', '-4/5']

**Answer given:**
> The value of sinθ is -3/5, cosθ is -4/5, tanθ is 3/4, cotθ is 4/3, secθ is -5/4, and cosecθ is -5/3. 
Using the given tanθ = 3/4 and the identity 1 + tan²θ = sec²θ (Source: Trigonometric_Ratios_and_Identities, Page 4), we can find secθ. 
First, we find sec²θ = 1 + (3/4)² = 1 + 9/16 = 25/16, so secθ = ±√(25/16) = ±5/4. 
Since θ is in the III quadrant, secθ is negative, so secθ = -5/4. 
Then, using the identity cos²θ + sin²θ = 1 (which can be derived from the Pythagorean identity sin²θ + cos²θ = 1), and cosθ = 1/secθ = -4/5, we can find sinθ. 
We have sin²θ = 1 - cos²θ = 1 - (-4/5)² = 1 - 16/25 = 9/25, so sinθ = ±√(9/25) = ±3/5. 
Since θ is in the III quadrant, sinθ is negative, so sinθ = -3/5. 
Now, we can find the other trigonometric ratios: tanθ = 3/4 (given), cotθ = 1/tanθ = 4/3, and cosecθ = 1/sinθ = -5/3 (Source: Trigonometric_Ratios_and_Identities, Page 4).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 16 (score 0.442)
- Trigonometric_Ratios_and_Identities, page 1 (score 0.438)
- Trigonometric_Ratios_and_Identities, page 4 (score 0.434)

---

## Q18: Prove sin⁴θ+cos⁴θ=1−2sin²θcos²θ.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3]
**Expected facts:** ['(sin²θ + cos²θ)²', '2sin²θcos²θ']

**Answer given:**
> The equation sin⁴θ + cos⁴θ = 1 - 2sin²θcos²θ can be proven using the identity (a) sin(A + B) sin(A - B) = sin²A - sin²B = cos²B - cos²A, however, a more direct approach is to recognize that sin⁴θ + cos⁴θ is a sum of fourth powers of sine and cosine, which can be related to the Pythagorean identity (Source: Trigonometric_Ratios_and_Identities, Page 12). 
We start with the Pythagorean identity sin²θ + cos²θ = 1. 
Squaring both sides gives (sin²θ + cos²θ)² = 1², which expands to sin⁴θ + 2sin²θcos²θ + cos⁴θ = 1. 
Rearranging the terms yields sin⁴θ + cos⁴θ = 1 - 2sin²θcos²θ, thus proving the given equation (Source: Trigonometric_Ratios_and_Identities, Page 12).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 12 (score 0.495)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.459)
- Trigonometric_Ratios_and_Identities, page 20 (score 0.433)

---

## Q19: Find the maximum value of 3sinx+4cosx.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [22, 23]
**Expected facts:** ['5']

**Answer given:**
> The maximum value of 3sinx + 4cosx is 5. 
To find the maximum value, we can use the method of making a perfect square in sine and cosine, as seen in [Source: Trigonometric_Ratios_and_Identities, Page 23]. 
We can express 3sinx + 4cosx as √(3² + 4²) (3/√(3² + 4²) sinx + 4/√(3² + 4²) cosx) = 5 (3/5 sinx + 4/5 cosx). 
Since 3/5 and 4/5 can be expressed as sinθ and cosθ for some θ, we can rewrite the expression as 5 (sinθ sinx + cosθ cosx) = 5 cos(x - θ), which has a maximum value of 5 (Source: Trigonometric_Ratios_and_Identities, Page 24).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 24 (score 0.51)
- Trigonometric_Ratios_and_Identities, page 23 (score 0.468)
- Trigonometric_Ratios_and_Identities, page 21 (score 0.462)

---

## Q20: Solve sinx=√3/2 for 0≤x≤2π.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ❌ MISS | **Faithfulness:** 50% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [4]
**Expected facts:** ['π/3', '2π/3']

**Answer given:**
> The solution to sinx = √3/2 for 0 ≤ x ≤ 2π is x = π/3 or x = 2π - π/3 = 5π/3. (Source: Trigonometric_Ratios_and_Identities, standard angle values are implied but not explicitly stated on the provided pages, however, standard angle values such as sin(π/3) = √3/2 are well-known and can be applied here).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 13 (score 0.464)
- Trigonometric_Ratios_and_Identities, page 23 (score 0.426)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.421)

---

## Q21: Evaluate cos(−300°).

**Type:** computational | **Difficulty:** easy | **Retrieval:** ❌ MISS | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['1/2']

**Answer given:**
> The value of cos(−300°) is cos(360° - 60°) = cos(60°) = 0.5 (Source: Trigonometric_Ratios_and_Identities, Page 17).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 17 (score 0.571)
- Trigonometric_Ratios_and_Identities, page 13 (score 0.537)
- Trigonometric_Ratios_and_Identities, page 16 (score 0.482)

---

## Q22: Find the period of y=tan(3x−π/6).

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [7, 8]
**Expected facts:** ['π/3']

**Answer given:**
> The period of y = tan(3x - π/6) is 2π/3, since the standard period of tan(x) is π (Source: Trigonometric_Ratios_and_Identities, Page 5), and the coefficient of x is 3, so the period is π/3, but considering the general form of tan(ax + b), the period is π/a (Source: Trigonometric_Ratios_and_Identities, Page 6), hence the period of y = tan(3x - π/6) is π/3. However, the given context does not explicitly provide the period of tan(ax + b) as π/a, but based on the properties of the tangent function, we can derive that the period of y = tan(3x - π/6) is π/3, but to be precise with the provided context, we should consider the period of tan(x) and its transformation. The period of tan(x) is π (Source: Trigonometric_Ratios_and_Identities, Page 5), and for tan(3x - π/6), the period would be π divided by the coefficient of x, hence the period is π/3, but the context does provide the transformation of tan(x) to tan(90° + x) = -cot(x) (Source: Trigonometric_Ratios_and_Identities, Page 6), which implies the period of tan(x) is π, so for tan(3x - π/6), it is π/3, but to be more accurate with the provided context, we should consider the period of tan(x) as π (Source: Trigonometric_Ratios_and_Identities, Page 5) and its transformation, hence the period of y = tan(3x - π/6) is actually π/3, which can also be represented as 2π/3 * (1/2) = π/3 * (2/2) = 2π/3 * 1/2 = π/3, but the correct interpretation of the period of tan(3x - π/6) based on the provided context is π/3, which can be simplified to 2π/3 * 1/2, but the correct and simplified answer is π/3, however, considering the provided context and standard trigonometric properties, the period of y = tan(3x - π/6) is actually π/3.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 17 (score 0.427)
- Trigonometric_Ratios_and_Identities, page 5 (score 0.42)
- Trigonometric_Ratios_and_Identities, page 6 (score 0.393)

---

## Q23: Show that tan²θ−sin²θ=sin⁴θ sec²θ.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [3]
**Expected facts:** ['sin⁴θ/cos²θ']

**Answer given:**
> The equation tan²θ - sin²θ = sin⁴θ sec²θ can be proven using the identities from the context. 
First, we can express tan²θ as sec²θ - 1 (Source: Trigonometric_Ratios_and_Identities, Page 3), so tan²θ - sin²θ = sec²θ - 1 - sin²θ. 
Then, using the identity sin²θ + cos²θ = 1 (Source: Trigonometric_Ratios_and_Identities, Page 3), we can rewrite this as sec²θ - (1 - cos²θ) - sin²θ = sec²θ - 1 + cos²θ - sin²θ. 
Since sec²θ = 1 + tan²θ (Source: Trigonometric_Ratios_and_Identities, Page 3) and tan²θ = sin²θ / cos²θ, we have sec²θ = 1 + sin²θ / cos²θ. 
Substituting this into our equation gives us (1 + sin²θ / cos²θ) - 1 + cos²θ - sin²θ = sin²θ / cos²θ + cos²θ - sin²θ = sin²θ / cos²θ - sin²θ(1 - cos²θ / sin²θ) = sin²θ / cos²θ - sin²θ(1 - 1 / (sin²θ / cos²θ)) = sin²θ / cos²θ - sin²θ + sin²θ cos²θ / sin²θ = sin²θ / cos²θ - sin²θ + cos²θ = sin²θ / cos²θ - sin²θ(1 - cos²θ) = sin²θ / cos²²θ = sin⁴θ sec²θ. 
Therefore, tan²θ - sin²θ = sin⁴θ sec²θ (Source: Trigonometric_Ratios_and_Identities, Page 3).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 12 (score 0.408)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.391)
- Trigonometric_Ratios_and_Identities, page 3 (score 0.364)

---

## Q24: Evaluate Σ: cos20°+cos40°+cos140°+cos160°.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['0']

**Answer given:**
> The value of Σ: cos20°+cos40°+cos140°+cos160° is 0. 
Using the identity from [Source: Trigonometric_Ratios_and_Identities, Page 13], we can write cos20° + cos40° = 2cos(30°)cos(10°) and cos140° + cos160° = 2cos(150°)cos(10°). 
Then, Σ = 2cos(30°)cos(10°) + 2cos(150°)cos(10°) = 2cos(10°)[cos(30°) + cos(150°)]. 
Again, using the same identity, cos(30°) + cos(150°) = 2cos(90°)cos(60°) = 0, since cos(90°) = 0. 
Therefore, Σ = 2cos(10°)*0 = 0 (Source: Trigonometric_Ratios_and_Identities, Page 13).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 13 (score 0.579)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.527)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.491)

---

## Q25: A point on the unit circle has y=−4/5 in quadrant IV. Find all trigonometric ratios.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [5]
**Expected facts:** ['3/5', '-4/3']

**Answer given:**
> The point has a y-coordinate of -4/5, so sin(θ) = -4/5, and since it's on the unit circle, we can use the identity sin^2(θ) + cos^2(θ) = 1 to find cos(θ) = ±√(1 - (-4/5)^2) = ±3/5, but since the point is in quadrant IV, cos(θ) is positive, so cos(θ) = 3/5 (Source: Trigonometric_Ratios_and_Identities, Page 6). 
Then, tan(θ) = sin(θ)/cos(θ) = (-4/5)/(3/5) = -4/3 (Source: Trigonometric_Ratios_and_Identities, Page 6). 
Also, cosec(θ) = 1/sin(θ) = -5/4, sec(θ) = 1/cos(θ) = 5/3, and cot(θ) = 1/tan(θ) = -3/4 (Source: Trigonometric_Ratios_and_Identities, Page 6).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 6 (score 0.48)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.462)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.449)

---

## Q26: Solve x²−7x+10=0.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [1]
**Expected facts:** ['x = 2', 'x = 5']

**Answer given:**
> The equation x²−7x+10=0 has roots that can be found using the relation between roots and coefficients of a quadratic equation, where the sum of the roots (x₁ + x₂) = -b/a and the product of the roots (x₁ * x₂) = c/a (Source: Quadratic_Equations, Page 2). 
Given the equation x² - 7x + 10 = 0, we can identify a = 1, b = -7, and c = 10. 
Using the formula, the sum of the roots is -(-7)/1 = 7 and the product of the roots is 10/1 = 10. 
We can then use these values to factor the quadratic equation or use the quadratic formula to find the roots. 
However, since we are given a simple quadratic equation, we can factor it directly as (x - 2)(x - 5) = 0, which gives us the roots x = 2 or x = 5. 
Therefore, the roots of the equation are x = 2 or x = 5.

**Chunks actually retrieved:**
- Quadratic_Equations, page 1 (score 0.403)
- Quadratic_Equations, page 2 (score 0.345)
- Quadratic_Equations, page 6 (score 0.323)

---

## Q27: Find the quadratic equation whose roots are 3 and −5.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['x² + 2x - 15']

**Answer given:**
> The quadratic equation whose roots are 3 and −5 is x² - (3 + (-5))x + (3 * (-5)) = 0, which simplifies to x² + 2x - 15 = 0 (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.483)
- Quadratic_Equations, page 1 (score 0.454)
- Quadratic_Equations, page 2 (score 0.423)

---

## Q28: If roots are α,β with α+β=8 and αβ=12, form the equation.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['x² - 8x + 12']

**Answer given:**
> The quadratic equation with roots α and β is x² - (α + β)x + αβ = 0, which simplifies to x² - 8x + 12 = 0 (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 12 (score 0.476)
- Quadratic_Equations, page 1 (score 0.454)
- Quadratic_Equations, page 2 (score 0.442)

---

## Q29: Determine the nature of roots of 2x²+4x+5=0.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['no real roots', '-24']

**Answer given:**
> The equation 2x²+4x+5=0 has no real roots, as the discriminant D = b² - 4ac = 4² - 4*2*5 = 16 - 40 = -24 < 0 (Source: Quadratic_Equations, Page 1).

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.511)
- Quadratic_Equations, page 2 (score 0.493)
- Quadratic_Equations, page 1 (score 0.463)

---

## Q30: If one root of x²−5x+k=0 is 2, find k.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [1, 2]
**Expected facts:** ['k = 6']

**Answer given:**
> The value of k is 2, since if one root of the equation x² - 5x + k = 0 is 2, we can use the fact that if a is a root of the quadratic equation ax² + bx + c = 0, then a satisfies the equation, so 2² - 5(2) + k = 0 (Source: Quadratic_Equations, Page 1). Solving for k, we get 4 - 10 + k = 0, which simplifies to k = 6.

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.477)
- Quadratic_Equations, page 2 (score 0.463)
- Quadratic_Equations, page 1 (score 0.447)

---

## Q31: Find k so that x²+kx+9=0 has equal roots.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['k = 6', 'k = -6']

**Answer given:**
> The value of k is 0 or 0, since for a quadratic equation ax² + bx + c = 0 to have equal roots, its discriminant b² - 4ac must be equal to 0 (Source: Quadratic_Equations, Page 5), so k² - 4*1*9 = 0, which simplifies to k² = 36, and hence k = 6 or k = -6, but for the given equation x² + kx + 9 = 0 to have equal roots, we must have k² - 4*1*9 = 0, which means k² = 36, so k = 6 or k = -6, but since b² - 4ac = k² - 4*1*9 = 0, then k = ±√(4*1*9) = ±6, so k = 6 or k = -6. 
However, the equation x² + kx + 9 = 0 has equal roots when its discriminant is zero, so k² - 4ac = 0, hence k² - 4*1*9 = 0, which gives k² = 36, and thus k = 6 or k = -6. 
Therefore, k = 6 or k = -6. (Source: Quadratic_Equations, Page 2)

**Chunks actually retrieved:**
- Quadratic_Equations, page 2 (score 0.429)
- Quadratic_Equations, page 5 (score 0.416)
- Quadratic_Equations, page 1 (score 0.403)

---

## Q32: If α,β are roots of x²−6x+5=0, find α²+β².

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2, 11]
**Expected facts:** ['26']

**Answer given:**
> α² + β² = (α + β)² - 2αβ = (-(-6))² - 2(5) = 36 - 10 = 26. 
This is derived from the relation between roots and coefficients of a quadratic equation, where α + β = -b/a and αβ = c/a (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.498)
- Quadratic_Equations, page 1 (score 0.426)
- Quadratic_Equations, page 2 (score 0.419)

---

## Q33: Find equation whose roots are reciprocals of roots of 2x²−3x−2=0.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [3]
**Expected facts:** ['2x² + 3x - 2']

**Answer given:**
> The equation whose roots are reciprocals of the roots of 2x² - 3x - 2 = 0 is 2x² - 3x - 2 = 0 transformed into 2(1/x)² - 3(1/x) - 2 = 0, which simplifies to 2 - 3x - 2x² = 0, and rearranging gives 2x² - 3x - 2 = 0 becomes -2x² + 3x + 2 = 0, but to get the correct form, we use the relation between roots and coefficients (Source: Quadratic_Equations, Page 2), if a, B are the roots of the original equation, then 1/a + 1/B = -(-3/2) and (1/a)*(1/B) = -2/2, which simplifies to 1/a + 1/B = 3/2 and 1/(a*B) = -1, so the equation whose roots are 1/a and 1/B is x² - (sum of roots)x + product of roots = 0, which becomes x² - (3/2)x - 1 = 0, then multiplying through by 2 to clear the fraction gives 2x² - 3x - 2 = 0, but this is the original equation, so we use the fact that if the roots of the quadratic equation are reciprocals of the original roots, then the new equation is 2x² - 3x - 2 = 0 transformed by the relations of the roots (Source: Quadratic_Equations, Page 2), which means the equation whose roots are the reciprocals is actually 2x² - 3x - 2 = 0 becomes 2(1/x)² - 3(1/x) - 2 = 0 and simplifying this expression we get 2 - 3x - 2x² = 0 and rearranging we have 2x² + 3x - 2 = 0, but to get the equation in standard form with the correct coefficients we apply the transformation directly to the original equation 2x² - 3x - 2 = 0 to obtain the equation whose roots are the reciprocals, which is 2x² + 3x - 2 = 0, however the correct transformation using the relation between roots and coefficients is x² - (sum of roots)x + product of roots = 0 (Source: Quadratic_Equations, Page 2), so for the reciprocals of the roots of 2x² - 3x - 2 = 0 we have the sum of the reciprocals of the roots (3/2) and the product of the reciprocals of the roots (-

**Chunks actually retrieved:**
- Quadratic_Equations, page 2 (score 0.537)
- Quadratic_Equations, page 1 (score 0.517)
- Quadratic_Equations, page 4 (score 0.44)

---

## Q34: Find minimum value of x²−8x+20.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [6, 7]
**Expected facts:** ['4']

**Answer given:**
> The minimum value of x² − 8x + 20 is  -12, when x = 4, since this is a quadratic equation and its minimum value can be found by completing the square or using the vertex formula (Source: Quadratic_Equations, Page 1).

**Chunks actually retrieved:**
- Quadratic_Equations, page 9 (score 0.403)
- Quadratic_Equations, page 1 (score 0.399)
- Trigonometric_Ratios_and_Identities, page 24 (score 0.391)

---

## Q35: Find maximum value of −2x²+12x−5.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [6, 7]
**Expected facts:** ['13']

**Answer given:**
> The maximum value of −2x² + 12x - 5 is 19. 
To find the maximum value, we can complete the square or use the formula for the vertex of a quadratic function (Source: Quadratic_Equations, Page 7). 
The given quadratic function can be rewritten as −2(x² - 6x) - 5. 
Completing the square, we get −2(x² - 6x + 9) - 5 + 18, which simplifies to −2(x - 3)² + 13. 
Since the coefficient of the squared term is negative, the maximum value occurs at the vertex, which is when x = 3. 
Substituting x = 3 into the original equation, we get −2(3)² + 12(3) - 5 = −18 + 36 - 5 = 13. 
However, we can also find the maximum value using the formula for the vertex, which is given by y = −2(x - h)² + k, where (h, k) is the vertex. 
In this case, h = −b / 2a = 6 / (2 * −2) = 3 and k = −2(3)² + 12(3) - 5 = 13, but since the quadratic opens downwards, the actual maximum is at the vertex and its value can also be found by using the formula for the x-coordinate of the vertex and then plugging it back into the equation to find the corresponding y-coordinate (Source: Quadratic_Equations, Page 7), which results in the same value of 13 + 6 = 19 (Source: Quadratic_Equations, Page 9).

**Chunks actually retrieved:**
- Quadratic_Equations, page 9 (score 0.447)
- Quadratic_Equations, page 7 (score 0.391)
- Trigonometric_Ratios_and_Identities, page 23 (score 0.39)

---

## Q36: Solve inequality x²−5x+6>0.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [6, 7]
**Expected facts:** ['x < 2', 'x > 3']

**Answer given:**
> The solution to the inequality x² - 5x + 6 > 0 is x ∈ (-∞, 2) ∪ (3, ∞), since the quadratic expression can be factored as (x - 2)(x - 3) > 0, which is true when both factors are negative or both are positive (Source: Quadratic_Equations, Page 7).

**Chunks actually retrieved:**
- Quadratic_Equations, page 7 (score 0.48)
- Quadratic_Equations, page 1 (score 0.412)
- Quadratic_Equations, page 8 (score 0.353)

---

## Q37: Solve |x²−4|<5.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [7, 8]
**Expected facts:** ['-3', '3']

**Answer given:**
> The solution to |x²−4|<5 is -1 < x < 3 and -√9 < x < √9, which simplifies to -1 < x < 3 and -3 < x < 3, so the combined solution is -1 < x < 3 (Source: Quadratic_Equations, Page 8), using the property of modulus function |x| <a => x € [-a, a] (Source: Quadratic_Equations, Page 8).

**Chunks actually retrieved:**
- Quadratic_Equations, page 7 (score 0.426)
- Quadratic_Equations, page 1 (score 0.356)
- Quadratic_Equations, page 8 (score 0.336)

---

## Q38: If α,β are roots of x²+px+6=0 and α²+β²=13, find p.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2, 11]
**Expected facts:** ['p = 5', 'p = -5']

**Answer given:**
> The value of p is -5, since we know that α + β = -p and αβ = 6 (Source: Quadratic_Equations, Page 2), and given α² + β² = 13, we can use the identity α² + β² = (α + β)² - 2αβ to find p, which gives us (α + β)² - 2αβ = 13, so (-p)² - 2(6) = 13, simplifying to p² - 12 = 13, then p² = 25, and p = ±5, but since α + β = -p, and we know α² + β² = (α + β)² - 2αβ, we can determine that α + β must be -5 (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.493)
- Quadratic_Equations, page 3 (score 0.376)
- Quadratic_Equations, page 2 (score 0.36)

---

## Q39: Find remainder when f(x)=x³−2x+5 is divided by x−2.

**Type:** computational | **Difficulty:** easy | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2, 3]
**Expected facts:** ['9']

**Answer given:**
> The remainder when f(x) = x³ - 2x + 5 is divided by x - 2 is f(2) = 2³ - 2*2 + 5 = 8 - 4 + 5 = 9 (Source: Quadratic_Equations, Page 1).

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.293)
- Quadratic_Equations, page 9 (score 0.265)
- Quadratic_Equations, page 1 (score 0.237)

---

## Q40: Find condition for ax²+bx+c to be always positive.

**Type:** conceptual | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 50% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [6, 7]
**Expected facts:** ['a > 0', 'D < 0']

**Answer given:**
> The quadratic equation ax² + bx + c = 0 has no condition to be always positive, however, we can derive a condition from the relation between roots and coefficients (Source: Quadratic_Equations, Page 2). For the quadratic equation to be always positive, it should have no real roots, which implies that the discriminant b² - 4ac < 0, but this condition is not explicitly mentioned in the context. However, we can say that if the quadratic equation has no real roots, then a > 0, since the graph of the quadratic equation will be entirely above the x-axis (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 1 (score 0.497)
- Quadratic_Equations, page 2 (score 0.491)
- Quadratic_Equations, page 4 (score 0.466)

---

## Q41: Find quadratic equation whose roots are α+1 and β+1 if α,β are roots of x²−4x+1=0.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [3]
**Expected facts:** ['x² - 6x + 6']

**Answer given:**
> The quadratic equation whose roots are α+1 and β+1 is x² - 2x - 3 = 0. 
Using the relation between roots and coefficients of a quadratic equation (Source: Quadratic_Equations, Page 2), we know that the sum of the roots is -b/a and the product of the roots is c/a. 
Given that α and β are the roots of x² - 4x + 1 = 0, we have α + β = 4 and αβ = 1. 
The sum of the new roots (α+1) and (β+1) is (α+1) + (β+1) = α + β + 2 = 4 + 2 = 6, and the product of the new roots is (α+1)(β+1) = αβ + α + β + 1 = 1 + 4 + 1 = 6. 
Therefore, the new quadratic equation is x² - (sum of roots)x + (product of roots) = 0, which becomes x² - 6x + 6 = 0, but since the original equation was x² - 4x + 1 = 0, and we added 1 to each root, we can also find the equation by using the transformation of the equation (Source: Quadratic_Equations, Page 1), however the direct calculation gives x² - (α+1+β+1)x + (α+1)(β+1) = x² - (α+β+2)x + (αβ+α+β+1) = x² - (4+2)x + (1+4+1) = x² - 6x + 6, but considering the standard form of a quadratic equation x² - (sum of roots)x + (product of roots) = 0, and given that the sum of roots is 6 and product of roots is not -3, we should look for an equation in the form x² - (α+1+β+1)x + (α+1)(β+1) = 0, and since α+β = 4, and αβ = 1, then (α+1)(β+1) = αβ + α + β + 1 = 1 + 4 + 1 = 6, and (α+1) + (β+1) = α + β + 2 = 4 + 2 = 6, hence x² - 6x + 6 = 0 is not the correct equation, we made a mistake, the correct sum is 6, but the product is (α+1)(β+1) = αβ + α + β + 1 = 1 + 4 + 1 = 6, so x²

**Chunks actually retrieved:**
- Quadratic_Equations, page 1 (score 0.472)
- Quadratic_Equations, page 5 (score 0.444)
- Quadratic_Equations, page 2 (score 0.442)

---

## Q42: Find value of m so x²−2mx+m+5=0 has no real roots.

**Type:** computational | **Difficulty:** hard | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2]
**Expected facts:** ['√21']

**Answer given:**
> The value of m is such that the discriminant b² - 4ac < 0, so for the equation x² - 2mx + m + 5 = 0, we have a = 1, b = -2m, and c = m + 5, hence (-2m)² - 4(1)(m + 5) < 0, which simplifies to 4m² - 4m - 20 < 0 (Source: Quadratic_Equations, Page 5), thus m² - m - 5 < 0. 
To solve the inequality m² - m - 5 < 0, we can factor it or complete the square, but since it doesn't factor easily, using the quadratic formula to find the roots of m² - m - 5 = 0 gives m = (1 ± √(1 + 20))/2 = (1 ± √21)/2 (Source: Quadratic_Equations, Page 2), and since the parabola opens upwards (a > 0), the inequality holds for (1 - √21)/2 < m < (1 + √21)/2, or approximately -1.79 < m < 2.79, but since we need the exact values, we keep (1 - √21)/2 < m < (1 + √21)/2.

**Chunks actually retrieved:**
- Quadratic_Equations, page 2 (score 0.459)
- Quadratic_Equations, page 5 (score 0.438)
- Quadratic_Equations, page 11 (score 0.425)

---

## Q43: If equations x²+3x+k=0 and x²+kx+3=0 have a common root, find k.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 0% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [4]
**Expected facts:** ['k = -4']

**Answer given:**
> The value of k for which the equations x²+3x+k=0 and x²+kx+3=0 have a common root is k = 3 or k = -3, (Source: Quadratic_Equations, Page 4). 

To find this, we use the condition for common roots: 
a₁a₂ - b₁b₂ = a₁c₂ - a₂c₁, 
where a₁ = 1, b₁ = 3, c₁ = k, a₂ = 1, b₂ = k, c₂ = 3. 
Substituting these values into the equation gives 
1*1 - 3*k = 1*3 - 1*k, 
which simplifies to 
1 - 3k = 3 - k, 
and further simplifies to 
-2k = 2, 
so k = -1 is not a solution, but rather k = 3 or k = -3 when using the quadratic formula and comparing roots directly (Source: Quadratic_Equations, Page 4).

**Chunks actually retrieved:**
- Quadratic_Equations, page 4 (score 0.501)
- Quadratic_Equations, page 5 (score 0.478)
- Quadratic_Equations, page 1 (score 0.38)

---

## Q44: Sketch the graph of y=x²−4x+3 and identify vertex and x-intercepts.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 33% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [6, 7]
**Expected facts:** ['(2, -1)', 'x = 1', 'x = 3']

**Answer given:**
> The graph of y = x² - 4x + 3 is a parabola that opens upwards since the coefficient of x² is positive (Source: Quadratic_Equations, Page 6). To find the vertex, we use the formula x = -b / 2a, where a = 1 and b = -4, so x = -(-4) / (2*1) = 4 / 2 = 2 (Source: Quadratic_Equations, Page 1). The y-coordinate of the vertex is y = (2)² - 4(2) + 3 = 4 - 8 + 3 = -1. Therefore, the vertex is at (2, -1). The x-intercepts can be found by solving the equation x² - 4x + 3 = 0 using the quadratic formula: x = (-b ± √(b² - 4ac)) / 2a, where a = 1, b = -4, and c = 3 (Source: Quadratic_Equations, Page 1). This gives x = (4 ± √((-4)² - 4*1*3)) / 2*1 = (4 ± √(16 - 12)) / 2 = (4 ± √4) / 2 = (4 ± 2) / 2, so x = (4 + 2) / 2 = 3 or x = (4 - 2) / 2 = 1. Therefore, the x-intercepts are at (1, 0) and (3, 0).

**Chunks actually retrieved:**
- Quadratic_Equations, page 6 (score 0.467)
- Quadratic_Equations, page 1 (score 0.39)
- Quadratic_Equations, page 7 (score 0.388)

---

## Q45: If roots of x²−9x+20=0 are α,β, compute α³+β³.

**Type:** computational | **Difficulty:** medium | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Quadratic_Equations, page(s) [2, 11]
**Expected facts:** ['189']

**Answer given:**
> α³ + β³ = (α + β)³ - 3αβ(α + β) = (9)³ - 3(20)(9) = 729 - 540 = 189. 
This is derived using the relation between roots and coefficients of a quadratic equation, where α + β = -(-9) = 9 and αβ = 20 (Source: Quadratic_Equations, Page 2).

**Chunks actually retrieved:**
- Quadratic_Equations, page 5 (score 0.452)
- Quadratic_Equations, page 2 (score 0.401)
- Quadratic_Equations, page 1 (score 0.398)

---

## Q46: Evaluate cos 130 degree.

**Type:** computational | **Difficulty:** hard | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['cos 50', '-0.64']

**Answer given:**
> The value of cos 130 degree is -cos 50 degree = -0.64 (Source: Trigonometric_Ratios_and_Identities, Page 17).

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 17 (score 0.535)
- Trigonometric_Ratios_and_Identities, page 13 (score 0.522)
- Trigonometric_Ratios_and_Identities, page 18 (score 0.519)

---

## Q47: Evaluate cos 100 degrees.

**Type:** computational | **Difficulty:** hard | **Retrieval:** ✅ HIT | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['cos 80', '-0.17']

**Answer given:**
> The value of cos 100 degrees can be evaluated using the identity cos(C) = cos(180° - C) = -cos(C) (Source: Trigonometric_Ratios_and_Identities, Page 7), so cos 100 degrees = -cos(100°) = -cos(180° - 80°) = -(-cos 80°) = cos 80°, but since we cannot find the exact value of cos 80° directly, we can use the identity cos C + cos D = 2cos((C+D)/2)cos((C-D)/2) (Source: Trigonometric_Ratios_and_Identities, Page 13) with C = 80° and D = 0° to get an expression for cos 80°, however, this approach doesn't lead to a straightforward solution. Alternatively, recognizing that cos(100°) = cos(90° + 10°) and using the identity cos(90° + θ) = -sin(θ) (Source: Trigonometric_Ratios_and_Identities, Page 7), we find cos 100 degrees = -sin 10 degrees, and since sin(10°) is not a standard angle, its decimal approximation is -sin(10°) = -0.17.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 17 (score 0.573)
- Trigonometric_Ratios_and_Identities, page 7 (score 0.531)
- Trigonometric_Ratios_and_Identities, page 13 (score 0.525)

---

## Q48: Evaluate sin 200 degrees.

**Type:** computational | **Difficulty:** hard | **Retrieval:** ❌ MISS | **Faithfulness:** 100% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['sin 20', '-0.34']

**Answer given:**
> The value of sin 200 degrees can be evaluated using the identity sin(A + B) = sinAcosB + cosAsinB (Source: Trigonometric_Ratios_and_Identities, Page 12), by expressing 200 degrees as the sum of 150 degrees and 50 degrees, however, a more direct approach is using the identity sin(180 - A) = sinA. 
So, sin 200 degrees = sin(180 + 20) degrees = -sin 20 degrees. 
To find the value of sin 20 degrees, we can use the identity sin(A) = cos(90 - A) (not directly provided but can be inferred from the given context), thus sin 20 degrees = cos(90 - 20) = cos 70 degrees. 
However, the exact value of cos 70 degrees is not directly provided, but we can use the given information to find the value of sin 20 degrees or cos 70 degrees. 
Given that sin 15 degrees and cos 15 degrees are provided in terms of radicals (Source: Trigonometric_Ratios_and_Identities, Page 12), we can use the identity sin(A + B) = sinAcosB + cosAsinB to find sin 20 degrees by expressing 20 degrees as 15 + 5 or other known angles, but the context does not provide a straightforward method to calculate sin 20 degrees. 
However, using the half-angle formula or other trigonometric identities that can be derived from the given context, we can find that sin 20 degrees is approximately equal to 0.34. 
Therefore, sin 200 degrees = -sin 20 degrees ≈ -0.34.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 13 (score 0.539)
- Trigonometric_Ratios_and_Identities, page 25 (score 0.518)
- Trigonometric_Ratios_and_Identities, page 12 (score 0.516)

---

## Q49: Evaluate tan 160 degrees.

**Type:** computational | **Difficulty:** hard | **Retrieval:** ✅ HIT | **Faithfulness:** 50% | **Refused:** False

**Expected source/page:** Trigonometric_Ratios_and_Identities, page(s) [6, 7]
**Expected facts:** ['tan 20', '-0.36']

**Answer given:**
> The value of tan 160 degrees is -tan 20 degrees, since tan(180° - θ) = -tan θ (Source: Trigonometric_Ratios_and_Identities, Page 7). To find the value of tan 20 degrees, we can use the identity tan θ = sin θ / cos θ, but the exact value of tan 20 degrees is not provided in the context. However, we can reduce it to tan 20 degrees = sin 20 degrees / cos 20 degrees, and using the given values, we can find the decimal approximation, tan 20 degrees ≈ sin 20 degrees / cos 20 degrees ≈ 0.364 / 0.94 ≈ 0.387, so tan 160 degrees ≈ -0.387.

**Chunks actually retrieved:**
- Trigonometric_Ratios_and_Identities, page 18 (score 0.556)
- Trigonometric_Ratios_and_Identities, page 7 (score 0.551)
- Trigonometric_Ratios_and_Identities, page 17 (score 0.531)

---
