from pathlib import Path
from datetime import datetime
import re
import os


# ============================================================
# PROJECT ROOT
# ============================================================

ROOT = Path(r"C:\Users\VEDANT\Desktop\ramjet")

# Output file created in the parent folder
OUTPUT_FILE = ROOT / "RAMJET_PROJECT_GUIDE.txt"


# ============================================================
# FILE TYPES
# ============================================================

TEXT_EXTENSIONS = {
    ".cfg", ".txt", ".py", ".geo", ".msh", ".su2",
    ".csv", ".log", ".dict", ".foam", ".json",
    ".xml", ".yaml", ".yml"
}

IMAGE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"
}

CAD_EXTENSIONS = {
    ".iges", ".igs", ".step", ".stp", ".x_t", ".x_b",
    ".sat", ".stl", ".prt", ".scdoc"
}

RESULT_EXTENSIONS = {
    ".csv", ".vtk", ".vtu", ".pvtu", ".dat", ".plt",
    ".cdat", ".log", ".his", ".history", ".su2"
}


# ============================================================
# KNOWN CASE FOLDER DESCRIPTIONS
# Based on the project folder names you provided.
# These descriptions are deliberately conservative.
# ============================================================

KNOWN_CASES = {
    "2d3dcompare":
        "Comparison/analysis of 2D and 3D CFD results.",

    "3d-no-slip":
        "3D no-slip CFD simulation case.",

    "3d-no-slip-mod":
        "Modified 3D no-slip CFD simulation case.",

    "extend 1 m, no slip":
        "Extended duct case with 1 m converging section plus downstream extension; no-slip configuration.",

    "extend 1 m, slip":
        "Extended duct case with 1 m converging section plus downstream extension; slip-wall configuration.",

    "extend 1.5 m":
        "Extended-duct simulation case. Exact extension/configuration should be confirmed from the case files.",

    "extend-1-m-no-slip-0.4":
        "Extended 1 m duct, no-slip case targeting approximately Mach 0.4.",

    "extend-1-m-no-slip-0.6":
        "Extended 1 m duct, no-slip case targeting approximately Mach 0.6.",

    "extend-1-m-slip-0.4":
        "Extended 1 m duct, slip-wall case targeting approximately Mach 0.4.",

    "extend-1-m-slip-0.6":
        "Extended 1 m duct, slip-wall case targeting approximately Mach 0.6.",

    "half gemetry":
        "Half-domain/half-geometry development case.",

    "mult domain":
        "Multi-domain/interface development case.",

    "openfoam":
        "OpenFOAM simulation and post-processing cases.",

    "random":
        "Miscellaneous/development files. Case purpose should be confirmed from individual files.",

    "results":
        "General CFD results/post-processing files.",

    "results-0.4":
        "Results associated with the Mach 0.4 case.",

    "results-0.6":
        "Results associated with the Mach 0.6 case.",

    "turb_0.01":
        "Turbulence-intensity case associated with 0.01 turbulence intensity.",

    "turb_5":
        "Turbulence-intensity case associated with 5% turbulence intensity.",
}


# ============================================================
# SAFE TEXT READING
# ============================================================

def read_text(path, max_chars=120000):
    """
    Reads only text-like files.
    Does not modify the file.
    """
    try:
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            return ""

        # Avoid reading extremely large files completely
        if path.stat().st_size > 5_000_000:
            with path.open("r", encoding="utf-8", errors="ignore") as f:
                return f.read(max_chars)

        with path.open("r", encoding="utf-8", errors="ignore") as f:
            return f.read(max_chars)

    except Exception:
        return ""


# ============================================================
# FILE TYPE
# ============================================================

def get_file_type(path):
    ext = path.suffix.lower()

    if ext in IMAGE_EXTENSIONS:
        return "Image / Figure"

    if ext in CAD_EXTENSIONS:
        return "CAD / Geometry"

    if ext in RESULT_EXTENSIONS:
        return "CFD Result / Data"

    if ext in {".py"}:
        return "Python Script"

    if ext in {".cfg"}:
        return "SU2 Configuration"

    if ext in {".geo"}:
        return "Gmsh Geometry Script"

    if ext in {".su2", ".msh"}:
        return "CFD Mesh"

    if ext in {".txt", ".log"}:
        return "Text / Log"

    if ext:
        return ext.upper()[1:] + " File"

    return "No Extension"


# ============================================================
# CASE INFORMATION CONTAINER
# ============================================================

def new_info():
    return {
        "solver": set(),
        "dimensions": set(),
        "wall": set(),
        "mach": set(),
        "turbulence": set(),
        "inlet_pressure": set(),
        "outlet_pressure": set(),
        "inlet_temperature": set(),
        "mesh": set(),
        "geometry": set(),
        "keywords": set(),
        "wall_function": False,
        "openfoam_wall_function": False,
        "files": [],
    }


# ============================================================
# DETECT INFORMATION FROM FILE CONTENT
# ============================================================

def analyse_content(text, path, info):

    low = text.lower()

    # --------------------------------------------------------
    # Solver
    # --------------------------------------------------------

    if "solver=" in low or "marker_inlet=" in low:
        info["solver"].add("SU2")

    if "fvschemes" in low or "fvsolution" in low:
        info["solver"].add("OpenFOAM")

    if "openfoam" in low:
        info["solver"].add("OpenFOAM")

    # --------------------------------------------------------
    # Dimension
    # --------------------------------------------------------

    if re.search(r"\bndime\s*=\s*3", low):
        info["dimensions"].add("3D")

    if re.search(r"\bndime\s*=\s*2", low):
        info["dimensions"].add("2D")

    if "three dimensional problem" in low:
        info["dimensions"].add("3D")

    if "two dimensional problem" in low:
        info["dimensions"].add("2D")

    # --------------------------------------------------------
    # SU2 wall conditions
    # --------------------------------------------------------

    if "marker_sym" in low:
        info["wall"].add("Botwall = Symmetry")

    if "marker_heatflux" in low:
        info["wall"].add("Heat-flux/no-slip wall")

    if "marker_euler" in low:
        info["wall"].add("Euler/slip wall")

    if "marker_wall_functions" in low:
        info["wall_function"] = True
        info["wall"].add("SU2 wall function")

    # --------------------------------------------------------
    # OpenFOAM wall functions
    # --------------------------------------------------------

    openfoam_wall_keywords = [
        "kqRWallFunction".lower(),
        "omegaWallFunction".lower(),
        "nutkWallFunction".lower(),
        "nutWallFunction".lower(),
        "epsilonWallFunction".lower()
    ]

    for keyword in openfoam_wall_keywords:
        if keyword.lower() in low:
            info["openfoam_wall_function"] = True
            info["wall"].add("OpenFOAM wall function")

    # --------------------------------------------------------
    # Turbulence
    # --------------------------------------------------------

    if "sst" in low:
        info["turbulence"].add("SST k-omega")

    if "freestream_turbulenceintensity" in low:

        match = re.search(
            r"freestream_turbulenceintensity\s*=\s*([0-9.eE+-]+)",
            text,
            re.IGNORECASE
        )

        if match:
            value = match.group(1)

            try:
                val = float(value)

                if val <= 1:
                    percent = val * 100
                    info["turbulence"].add(
                        f"Turbulence intensity = {val:g} ({percent:g}%)"
                    )
                else:
                    info["turbulence"].add(
                        f"Turbulence intensity = {val:g}%"
                    )

            except ValueError:
                pass

    # --------------------------------------------------------
    # Mach
    # --------------------------------------------------------

    mach_matches = re.findall(
        r"(?:mach(?:_number)?|ma)\s*=?\s*([0-9]+(?:\.[0-9]+)?)",
        text,
        re.IGNORECASE
    )

    for value in mach_matches:
        try:
            m = float(value)

            if 0.01 <= m <= 5.0:

                if abs(m - 0.4) < 0.02:
                    info["mach"].add("Mach ≈ 0.4")

                elif abs(m - 0.6) < 0.02:
                    info["mach"].add("Mach ≈ 0.6")

                elif abs(m - 0.95) < 0.03:
                    info["mach"].add("Mach ≈ 0.95")

        except ValueError:
            pass

    # --------------------------------------------------------
    # SU2 Inlet pressure and temperature
    # --------------------------------------------------------

    inlet_match = re.search(
        r"MARKER_INLET\s*=\s*\(\s*[^,]+,\s*"
        r"([0-9.eE+-]+)\s*,\s*"
        r"([0-9.eE+-]+)",
        text,
        re.IGNORECASE
    )

    if inlet_match:

        try:
            T = float(inlet_match.group(1))
            P = float(inlet_match.group(2))

            info["inlet_temperature"].add(
                f"{T:g} K"
            )

            info["inlet_pressure"].add(
                f"{P/1000:g} kPa"
            )

        except ValueError:
            pass

    # --------------------------------------------------------
    # SU2 Outlet pressure
    # --------------------------------------------------------

    outlet_match = re.search(
        r"MARKER_OUTLET\s*=\s*\(\s*[^,]+,\s*"
        r"([0-9.eE+-]+)",
        text,
        re.IGNORECASE
    )

    if outlet_match:

        try:
            P = float(outlet_match.group(1))

            info["outlet_pressure"].add(
                f"{P/1000:g} kPa"
            )

        except ValueError:
            pass

    # --------------------------------------------------------
    # Mesh filename
    # --------------------------------------------------------

    mesh_match = re.search(
        r"MESH_FILENAME\s*=\s*([^\s]+)",
        text,
        re.IGNORECASE
    )

    if mesh_match:
        info["mesh"].add(
            mesh_match.group(1).strip()
        )

    # --------------------------------------------------------
    # SU2 numerical settings
    # --------------------------------------------------------

    keywords_to_detect = [
        "JST",
        "ROE",
        "HLLC",
        "MUSCL",
        "GREEN_GAUSS",
        "EULER_IMPLICIT",
        "FGMRES",
        "PIMPLE",
        "Kurganov",
        "upwind",
        "vanAlbada",
        "limitedLinear",
        "Sutherland",
        "ideal_gas",
        "TIME_DOMAIN= NO",
        "TIME_DOMAIN= YES",
    ]

    for keyword in keywords_to_detect:

        if keyword.lower() in low:
            info["keywords"].add(keyword)


# ============================================================
# FOLDER ANALYSIS
# ============================================================

def analyse_folder(folder):

    info = new_info()

    try:
        files = sorted(
            [
                p for p in folder.rglob("*")
                if p.is_file()
            ],
            key=lambda p: str(p).lower()
        )

    except Exception:
        files = []

    for path in files:

        if path.resolve() == OUTPUT_FILE.resolve():
            continue

        try:
            size = path.stat().st_size
        except Exception:
            size = 0

        info["files"].append({
            "path": path,
            "type": get_file_type(path),
            "size": size
        })

        # File-name based detection
        name = path.name.lower()

        if "openfoam" in name:
            info["solver"].add("OpenFOAM")

        if "su2" in name:
            info["solver"].add("SU2")

        if "slip" in name and "no-slip" not in name:
            info["wall"].add("Slip wall")

        if "no-slip" in name or "noslip" in name:
            info["wall"].add("No-slip wall")

        if "0.4" in name:
            info["mach"].add("Mach ≈ 0.4")

        if "0.6" in name:
            info["mach"].add("Mach ≈ 0.6")

        if "0.95" in name:
            info["mach"].add("Mach ≈ 0.95")

        if "3d" in name:
            info["dimensions"].add("3D")

        if "2d" in name:
            info["dimensions"].add("2D")

        # File content
        text = read_text(path)

        if text:
            analyse_content(text, path, info)

    # Geometry indication
    for item in info["files"]:
        if item["type"] == "CAD / Geometry":
            info["geometry"].add(item["path"].name)

        if item["type"] == "Gmsh Geometry Script":
            info["geometry"].add(item["path"].name)

    return info


# ============================================================
# FORMAT HELPERS
# ============================================================

def human_size(size):

    if size < 1024:
        return f"{size} B"

    if size < 1024**2:
        return f"{size/1024:.1f} KB"

    if size < 1024**3:
        return f"{size/1024**2:.1f} MB"

    return f"{size/1024**3:.2f} GB"


def clean_set(values):

    if not values:
        return "Not detected"

    return "; ".join(
        sorted(values, key=str.lower)
    )


# ============================================================
# CREATE CASE DESCRIPTION
# ============================================================

def case_description(folder, info):

    folder_name = folder.name
    key = folder_name.lower()

    # Start with known project description
    description = KNOWN_CASES.get(
        key,
        "Case purpose detected from folder name and file contents."
    )

    details = []

    if info["dimensions"]:
        details.append(
            "Dimension: " + clean_set(info["dimensions"])
        )

    if info["solver"]:
        details.append(
            "Solver: " + clean_set(info["solver"])
        )

    if info["wall"]:
        details.append(
            "Wall treatment: " + clean_set(info["wall"])
        )

    if info["mach"]:
        details.append(
            "Mach case: " + clean_set(info["mach"])
        )

    if info["turbulence"]:
        details.append(
            "Turbulence: " + clean_set(info["turbulence"])
        )

    if info["inlet_pressure"]:
        details.append(
            "Inlet pressure: " +
            clean_set(info["inlet_pressure"])
        )

    if info["inlet_temperature"]:
        details.append(
            "Inlet temperature: " +
            clean_set(info["inlet_temperature"])
        )

    if info["outlet_pressure"]:
        details.append(
            "Outlet pressure: " +
            clean_set(info["outlet_pressure"])
        )

    if info["mesh"]:
        details.append(
            "Mesh: " + clean_set(info["mesh"])
        )

    if info["geometry"]:
        details.append(
            "Geometry files: " +
            clean_set(info["geometry"])
        )

    return description, details


# ============================================================
# WRITE PROJECT GUIDE
# ============================================================

def build_report():

    if not ROOT.exists():
        raise FileNotFoundError(
            f"Project folder not found:\n{ROOT}"
        )

    top_folders = sorted(
        [
            p for p in ROOT.iterdir()
            if p.is_dir()
        ],
        key=lambda p: p.name.lower()
    )

    top_files = sorted(
        [
            p for p in ROOT.iterdir()
            if p.is_file()
        ],
        key=lambda p: p.name.lower()
    )

    report = []

    report.append("=" * 80)
    report.append("RAMJET CFD PROJECT - FILE AND CASE HANDOVER GUIDE")
    report.append("=" * 80)
    report.append("")
    report.append(
        "Generated: " +
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    report.append("")
    report.append(
        "IMPORTANT: This report is generated automatically by reading "
        "the existing project files."
    )
    report.append(
        "No existing project file is moved, renamed, deleted, or modified."
    )
    report.append("")
    report.append(f"Project root: {ROOT}")
    report.append("")
    report.append("=" * 80)
    report.append("PROJECT OVERVIEW")
    report.append("=" * 80)
    report.append("")
    report.append(
        f"Number of case/result folders: {len(top_folders)}"
    )
    report.append(
        f"Number of files directly in root: {len(top_files)}"
    )
    report.append("")
    report.append(
        "The folder names are preserved exactly as they currently exist."
    )
    report.append(
        "Case descriptions are inferred from folder names and available "
        "configuration/result files."
    )
    report.append("")

    # ========================================================
    # TOP-LEVEL CASE SUMMARY
    # ========================================================

    report.append("=" * 80)
    report.append("CASE SUMMARY")
    report.append("=" * 80)
    report.append("")

    for folder in top_folders:

        info = analyse_folder(folder)

        description, details = case_description(
            folder,
            info
        )

        total_size = sum(
            item["size"]
            for item in info["files"]
        )

        report.append("-" * 80)
        report.append(f"CASE FOLDER: {folder.name}")
        report.append("-" * 80)
        report.append(f"Description: {description}")
        report.append(f"Total files: {len(info['files'])}")
        report.append(
            f"Total stored size: {human_size(total_size)}"
        )

        if not info["files"]:
            report.append("Status: Empty folder")

        for detail in details:
            report.append(detail)

        if info["wall_function"]:
            report.append(
                "SU2 wall-function marker detected."
            )

        if info["openfoam_wall_function"]:
            report.append(
                "OpenFOAM wall-function keywords detected."
            )

        report.append("")

    # ========================================================
    # ROOT FILES
    # ========================================================

    report.append("=" * 80)
    report.append("FILES DIRECTLY IN PROJECT ROOT")
    report.append("=" * 80)
    report.append("")

    for path in top_files:

        if path.resolve() == OUTPUT_FILE.resolve():
            continue

        try:
            size = path.stat().st_size
        except Exception:
            size = 0

        report.append(
            f"{path.name} | "
            f"{get_file_type(path)} | "
            f"{human_size(size)}"
        )

    report.append("")

    # ========================================================
    # FULL FILE INVENTORY
    # ========================================================

    report.append("=" * 80)
    report.append("FULL FILE INVENTORY")
    report.append("=" * 80)
    report.append("")
    report.append(
        "Each file is listed using its original relative path. "
        "Nothing has been moved or renamed."
    )
    report.append("")

    for folder in top_folders:

        info = analyse_folder(folder)

        report.append("")
        report.append(
            f"[{folder.name}]"
        )
        report.append("")

        for item in info["files"]:

            rel = item["path"].relative_to(ROOT)

            report.append(
                f"{rel} | "
                f"{item['type']} | "
                f"{human_size(item['size'])}"
            )

    # ========================================================
    # HANDOVER NOTES
    # ========================================================

    report.append("")
    report.append("=" * 80)
    report.append("HANDOVER NOTES FOR NEXT STUDENT")
    report.append("=" * 80)
    report.append("")
    report.append(
        "1. Preserve the existing folder names and file locations."
    )
    report.append(
        "2. Do not overwrite original CFD results when creating "
        "new simulations."
    )
    report.append(
        "3. SU2 configuration files (.cfg) contain the solver, "
        "boundary conditions and numerical settings."
    )
    report.append(
        "4. OpenFOAM cases should be interpreted using their "
        "controlDict, fvSchemes, fvSolution and 0/ field files."
    )
    report.append(
        "5. CSV files are generally sampled/post-processed CFD data."
    )
    report.append(
        "6. Mesh files should not be renamed unless a new case "
        "requires a separate mesh."
    )
    report.append(
        "7. For comparison studies, verify geometry, inlet/outlet "
        "conditions, turbulence model, wall treatment and sampling "
        "location before comparing results."
    )
    report.append(
        "8. Folder-name based descriptions are only preliminary; "
        "configuration files take priority when determining the "
        "actual simulation setup."
    )
    report.append("")
    report.append("=" * 80)
    report.append("END OF PROJECT GUIDE")
    report.append("=" * 80)

    OUTPUT_FILE.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print("")
    print("=" * 60)
    print("PROJECT INVENTORY CREATED")
    print("=" * 60)
    print(f"Output: {OUTPUT_FILE}")
    print("")
    print(
        "Existing files were NOT moved, renamed, deleted, "
        "or modified."
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    build_report()