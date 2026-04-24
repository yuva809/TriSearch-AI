"""
test_local.py — Local test runner.
Usage: python test_local.py
"""
from retrieve import retrieve, evaluate, _query_is_narrow

QUERIES = [
    # Broad
    "What was the main finding of the brand study?",
    "What are the cooking habits of probable trialists?",
    "How many respondents were surveyed?",
    "What channels do consumers use to buy frozen ready meals?",
    "What competitors appear in the frozen meal market?",
    # Narrow — long-form
    "What does the variable frm_brand_awareness measure?",
    "What does N_Home_Cooking_per_week mean?",
    "What does frm_brand_consideration capture?",
    "What are probable_trialists?",
    "What is total_count?",
    # Narrow — short (edge cases)
    "brand awareness",
    "frm_brand_consideration",
    "share of wallet",
    "cooking enjoyment",
]

print("=" * 70)
print("  RETRIEVAL TEST  (keyword scorer baseline)")
print("=" * 70)

for q in QUERIES:
    qtype = "narrow" if _query_is_narrow(q) else "broad"
    print(f"\nQ [{qtype:6}]: {q}")
    results = retrieve(q)
    for i, r in enumerate(results, 1):
        print(f"  {i}. [{r['source']:<35}] score={r['score']:.4f}")
        print(f"     {r['text'][:110]}…")

print("\n" + "=" * 70)
print("  EVALUATION METRICS  (MRR + P@1 on 14-query eval set)")
print("=" * 70)
metrics = evaluate()
print(f"\n  MRR = {metrics['MRR']}   P@1 = {metrics['P@1']}\n")
print(f"  {'Query':<47} {'Type':6} {'RR':>5}  {'P@1':>3}  Top source")
print("  " + "-" * 92)
for row in metrics["detail"]:
    q_short = row["query"][:46] + ("…" if len(row["query"]) > 46 else "")
    print(f"  {q_short:<47} {row['type']:6} {row['rr']:>5}  {row['p@1']:>3}  {row['top_src']}")
