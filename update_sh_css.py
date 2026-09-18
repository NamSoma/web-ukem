import os

file = r'f:\Back up อีก HDD\งาน\ลองทำ\css\global.css'

with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
for i, line in enumerate(lines):
    if '/* --- Stakeholder Analysis Redesign --- */' in line:
        start_idx = i
        break

if start_idx != -1:
    lines = lines[:start_idx]

new_css = """
/* --- Stakeholder Analysis Redesign --- */
stakeholder-card {
    display: block;
    margin-bottom: 0;
}

.sh-container {
    border-top: 2px solid var(--primary);
    margin-top: 40px;
    margin-bottom: 60px;
}

.sh-row {
    display: flex;
    padding: 40px 0;
    border-bottom: 1px solid #e2e8f0;
    background: transparent;
    transition: background-color 0.3s ease;
}

.sh-row:hover {
    background-color: rgba(241, 245, 249, 0.4);
}

.sh-title-col {
    flex: 0 0 25%;
    padding-right: 30px;
}

.sh-title {
    font-size: 26px;
    font-weight: 700;
    color: var(--primary);
    margin: 0;
    line-height: 1.3;
}

.sh-content-col {
    flex: 0 0 75%;
}

.sh-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.sh-col {
    display: flex;
    flex-direction: column;
}

.sh-col-title {
    color: #64748b;
    font-size: 14px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 0;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e2e8f0;
}

.sh-col-content ul {
    margin: 0;
    padding-left: 0;
    list-style: none;
    color: #334155;
    font-size: 16px;
    line-height: 1.6;
}

.sh-col-content ul li {
    margin-bottom: 12px;
    position: relative;
    padding-left: 20px;
}

.sh-col-content ul li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 9px;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--primary-light);
}

.sh-col-content ul li:last-child {
    margin-bottom: 0;
}

/* Dark mode support */
[data-theme="dark"] .sh-row {
    border-bottom-color: #374151;
}
[data-theme="dark"] .sh-row:hover {
    background-color: rgba(31, 41, 55, 0.5);
}
[data-theme="dark"] .sh-col-title {
    border-bottom-color: #374151;
    color: #9ca3af;
}
[data-theme="dark"] .sh-col-content ul {
    color: #e5e7eb;
}

/* Responsive */
@media (max-width: 992px) {
    .sh-row {
        flex-direction: column;
        padding: 30px 0;
    }
    
    .sh-title-col {
        flex: 0 0 100%;
        padding-right: 0;
        margin-bottom: 25px;
    }
    
    .sh-content-col {
        flex: 0 0 100%;
    }
    
    .sh-grid {
        grid-template-columns: 1fr;
        gap: 25px;
    }
}
"""

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)
    f.write(new_css)
    
print("CSS updated.")
