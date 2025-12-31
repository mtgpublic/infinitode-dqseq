# -*- coding: utf-8 -*-

import argparse
import re
from pathlib import Path
from typing import List, Tuple

_CJK_RE = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]")

def contains_cjk(text: str) -> bool:
    return _CJK_RE.search(text) is not None

def build_rules() -> List[Tuple[str, str]]:
    # (Chinese Abbreviation, English Abbreviation)
    rules = [
        ("核", "RCR"),
        ("紫", "ACR"),
        ("橙", "DCR"),
        ("伤害", "DMG"),
        ("攻速", "ASPD"),
        ("暴击", "CDMG"),
        ("易伤", "VULN"),
        ("时间", "DUR"),
        ("雷电", "LIT"),
        ("全技能", "AART"),
        ("策反", "ZMB"),
        ("技能", "AAC"),
        ("等级", "TLV"),
        ("矿等", "MLV"),
        ("赏金邻近", "BBNT"),
        ("赏金塔", "TBNT"),
        ("技能点", "AME"),
        ("随机技能", "RAT"),
        ("金币生成", "CGEN"),
        ("立即金币", "RCVC"),
        ("最后敌人", "LWND"),
        ("低血量敌人", "LHND"),
        ("双倍矿", "DMSP"),
        ("敌人爆炸", "FEWX"),
        ("基地爆炸", "BEXP"),
        ("随机矿", "RMIN"),
        ("平台", "RPLT"),
        ("双倍秒伤", "MDPS"),
        ("核弹", "NUKE"),
        ("额外掉落", "BELT"),
        ("双倍物品", "DLOT"),
        ("掉矿", "ERES"),
        ("挖青", "LEGI"),
        ("挖尘", "DUST"),
        ("头目", "BOSS"),
        ("挖怪", "MSE"),
        ("卖塔", "SELL"),
        ("加一", "MBVNT"),
        ("序列升级", "BPWR"),
        ("绿钞", "GP"),
        ("雷电减费", "AETHUN"),
        ("电球减费", "AELBLL"),
        ("激光减费", "AELOIC"),
        ("火球减费", "AEFBLL"),
        ("暴雪减费", "AEFRZ"),
        ("风暴减费", "AEWIND"),
        ("烈焰减费", "AEBURN"),
        ("毒气减费", "AEPOI"),
        ("磁铁减费", "AEMAG"),
        ("基础对冰", "BASICY"),
        ("基础对愈", "BASHEA"),
        ("基础对甲", "BASARM"),
        ("基础对紫", "BASFIG"),
        ("狙击对黄", "SNIFST"),
        ("狙击对毒", "SNITOX"),
        ("狙击对直升", "SNIHEL"),
        ("加农对壮", "CANSTR"),
        ("加农对毒", "CANTOX"),
        ("加农对甲", "CANARM"),
        ("加农对直升", "CANHEL"),
        ("寒冰对甲", "FRZARM"),
        ("寒冰对冰", "FRZICY"),
        ("寒冰对黄", "FRZFST"),
        ("毒液对冰", "VENICY"),
        ("毒液对黄", "VENFST"),
        ("毒液对毒", "VENTOX"),
        ("散射对绿", "SPLREG"),
        ("散射对喷气", "SPLJET"),
        ("散射对甲", "SPLARM"),
        ("爆破对壮", "BLASTR"),
        ("爆破对轻", "BLALIT"),
        ("爆破对冰", "BLAICY"),
        ("多重对愈", "MULHEA"),
        ("多重对紫", "MULFIG"),
        ("多重对甲", "MULARM"),
        ("机枪对壮", "MGNSTR"),
        ("机枪对头目", "MGNBOS"),
        ("机枪对轻", "MGNLIT"),
        ("防空对甲", "AIRARM"),
        ("防空对愈", "AIRHEA"),
        ("防空对头目", "AIRBOS"),
        ("防空对直升", "AIRHEL"),
        ("电塔对黄", "TSLFST"),
        ("电塔对直升", "TSLHEL"),
        ("电塔对甲", "TSLARM"),
        ("导弹对绿", "MSLREG"),
        ("导弹对黄", "MSLFST"),
        ("导弹对毒", "MSLTOX"),
        ("喷火对愈", "FLTHEA"),
        ("喷火对甲", "FLTARM"),
        ("喷火对黄", "FLTFST"),
        ("激光对愈", "LSRHEA"),
        ("激光对绿", "LSRREG"),
        ("激光对冰", "LSRICY"),
        ("高斯对黄", "GSSFST"),
        ("高斯对喷气", "GSSJET"),
        ("高斯对毒", "GSSTOX"),
        ("压碎对直升", "CRUHEL"),
        ("压碎对喷气", "CRUJET"),
        ("压碎对壮", "CRUSTR"),
    ]

    rules.sort(key=lambda x: (-len(x[0]), x[0]))
    return rules

def process_text(text: str, rules: List[Tuple[str, str]]) -> str:
    for zh, en in rules:
        text = text.replace(zh, f"{en}|")

    text = text.replace("|\t", "\t")
    text = text.replace("|\n", "\n")
    return text

def read_text_best_effort(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding="utf-8", errors="replace")

def main() -> int:
    parser = argparse.ArgumentParser(description="Replace Chinese abbreviations in .txt files from dir A into dir B.")
    parser.add_argument("dir_a", help="Source directory A")
    parser.add_argument("dir_b", help="Output directory B")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files, only print CJK paths if any")
    args = parser.parse_args()

    dir_a = Path(args.dir_a).resolve()
    dir_b = Path(args.dir_b).resolve()

    if not dir_a.is_dir():
        raise SystemExit(f"dir_a is not a directory: {dir_a}")

    rules = build_rules()

    for src in dir_a.rglob("*.txt"):
        if not src.is_file():
            continue

        rel = src.relative_to(dir_a)
        dst = dir_b / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        original = read_text_best_effort(src)
        processed = process_text(original, rules)

        if contains_cjk(processed):
            print(str(dst))

        if not args.dry_run:
            dst.write_text(processed, encoding="utf-8", newline="")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())