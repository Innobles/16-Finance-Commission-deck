import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find where Slide 10: CORE WORKFLOW begins (this is the old slide 10, which comes right after our new slide 7)
    s8_match = re.search(r'<!-- =================== SLIDE 10: CORE WORKFLOW =================== -->', html)
    if not s8_match:
        print("Could not find Slide 10: CORE WORKFLOW start")
        return
    
    html_up_to_s7 = html[:s8_match.start()]
    
    # Extract Slide 16 (Mobile App)
    s16_match = re.search(r'<!-- =================== SLIDE 16: MOBILE APP DEMO =================== -->(.*?)<!-- =================== SLIDE 17: LIVE DASHBOARD DEMO =================== -->', html, re.DOTALL)
    if not s16_match:
        print("Could not find Slide 16")
        return
    s16_html = s16_match.group(1)
    s16_html = s16_html.replace('id="s16"', 'id="s9"')
    s16_html = '<!-- =================== SLIDE 9: MOBILE APP DEMO =================== -->' + s16_html

    # Extract Slide 17 (Dashboard)
    s17_match = re.search(r'<!-- =================== SLIDE 17: LIVE DASHBOARD DEMO =================== -->(.*?)<!-- =================== SLIDE 18: PROOF OF WORK \(CREDIBILITY\) =================== -->', html, re.DOTALL)
    if not s17_match:
        print("Could not find Slide 17")
        return
    s17_html = s17_match.group(1)
    s17_html = s17_html.replace('id="s17"', 'id="s10"')
    s17_html = '<!-- =================== SLIDE 10: DASHBOARD DEMO =================== -->' + s17_html

    # Extract Slide 18 (PoW)
    s18_match = re.search(r'<!-- =================== SLIDE 18: PROOF OF WORK \(CREDIBILITY\) =================== -->(.*?)<!-- =================== SLIDE 19: CLOSING =================== -->', html, re.DOTALL)
    if not s18_match:
        print("Could not find Slide 18")
        return
    s18_html = s18_match.group(1)
    s18_html = s18_html.replace('id="s18"', 'id="s13"')
    s18_html = '<!-- =================== SLIDE 13: PROOF OF WORK =================== -->' + s18_html

    # Extract Slide 19 (Closing) + the rest of the file
    s19_match = re.search(r'<!-- =================== SLIDE 19: CLOSING =================== -->(.*)', html, re.DOTALL)
    if not s19_match:
        print("Could not find Slide 19")
        return
    s19_html = s19_match.group(1)
    s19_html = s19_html.replace('id="s19"', 'id="s20"')
    s19_html = '<!-- =================== SLIDE 20: CLOSING =================== -->' + s19_html

    
    # New Slide HTML blocks
    new_s8 = """
    <!-- =================== SLIDE 8: CORE WORKFLOW =================== -->
    <div class="slide" id="s8">
        <div class="bg-glow glow-3 pulse"></div>
        <p class="slide-tag">End-to-End Flow</p>
        <h2 class="slide-title">The 7-Step Operational Workflow</h2>
        <div class="grid-2" style="max-width:1050px;gap:30px">
            <div class="stagger" style="display:flex;flex-direction:column;gap:16px">
                <div class="flow-step">
                    <div class="flow-num" style="background:var(--axis)">1</div>
                    <div>
                        <h4>Biometric Job Selection</h4>
                        <p>Junior Engineer logs in; geo-fenced app reveals only locally approved, 16FC-compliant projects.</p>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-num" style="background:var(--axis)">2</div>
                    <div>
                        <h4>Tamper-Proof Evidence</h4>
                        <p>In-app camera enforces GPS coordinates, timestamps, and project IDs on all milestone photos.</p>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-num" style="background:var(--blue)">3</div>
                    <div>
                        <h4>AI Coordinate Validation</h4>
                        <p>Cloud middleware validates metadata against the sanctioned blueprint immediately.</p>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-num" style="background:var(--blue)">4</div>
                    <div>
                        <h4>Automated DPR Generation</h4>
                        <p>Digital Progress Report instantly queued on the Nodal Dashboard for review.</p>
                    </div>
                </div>
            </div>
            <div class="stagger" style="display:flex;flex-direction:column;gap:16px">
                <div class="flow-step">
                    <div class="flow-num" style="background:rgba(204,204,255,.8)">5</div>
                    <div>
                        <h4>Nodal Officer DSC Approval</h4>
                        <p>Officer verifies side-by-side evidence; signs off using legally binding Digital Signature (DSC).</p>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-num" style="background:var(--gold)">6</div>
                    <div>
                        <h4>Axis API Payment Trigger</h4>
                        <p>Verified XML payload pushed to Axis Bank CBS for immediate drawing limit check via PFMS.</p>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-num" style="background:var(--green)">7</div>
                    <div>
                        <h4>Direct Vendor Credit</h4>
                        <p>Central SNA debited, vendor credited seamlessly. Auto-reconciliation receipt pushes back to the dashboard.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

    new_s11_12 = """
    <!-- =================== SLIDE 11: 16FC GUIDELINES MAPPING =================== -->
    <div class="slide" id="s11">
        <div class="bg-glow glow-1 pulse"></div>
        <p class="slide-tag">Compliance Alignment</p>
        <h2 class="slide-title">16FC Guidelines &rarr; PLD Hub Mapping</h2>
        <p class="slide-subtitle">How our platform directly solves the mandatory compliance requirements for 16FC grant disbursals.</p>
        
        <table style="width:100%;max-width:1000px;margin-top:20px;border-collapse:collapse;color:#fff">
            <thead>
                <tr style="background:rgba(151,20,77,.2);border-bottom:2px solid var(--axis)">
                    <th style="padding:16px;text-align:left;font-family:var(--font-head)">16th FC Core Guideline</th>
                    <th style="padding:16px;text-align:left;font-family:var(--font-head)">PLD Intelligence Hub Solution</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom:1px solid var(--glass-border)">
                    <td style="padding:16px"><strong>100% Digital Geo-tagging required for all assets.</strong></td>
                    <td style="padding:16px;color:var(--gray)"><i class="fas fa-check-circle" style="color:var(--green)"></i> Camera-only module enforces unalterable GPS/Time metadata embedded in every submission.</td>
                </tr>
                <tr style="border-bottom:1px solid var(--glass-border)">
                    <td style="padding:16px"><strong>Eliminate idle float and parking of funds in accounts.</strong></td>
                    <td style="padding:16px;color:var(--gray)"><i class="fas fa-check-circle" style="color:var(--green)"></i> Just-In-Time (JIT) SNA/ZBSA architecture means funds stay in central earning accounts until exact disbursement second.</td>
                </tr>
                <tr style="border-bottom:1px solid var(--glass-border)">
                    <td style="padding:16px"><strong>Submission of audited UCs within strict deadlines.</strong></td>
                    <td style="padding:16px;color:var(--gray)"><i class="fas fa-check-circle" style="color:var(--green)"></i> Auto-generated, digitally signed (DSC) Progress Reports instantly bypass manual paperwork bottlenecks.</td>
                </tr>
                <tr>
                    <td style="padding:16px"><strong>Direct Benefit/Vendor Transfer integration with PFMS.</strong></td>
                    <td style="padding:16px;color:var(--gray)"><i class="fas fa-check-circle" style="color:var(--green)"></i> Native APIs directly command Axis CBS to hit PFMS for drawing limits and vendor RTGS routing.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- =================== SLIDE 12: AXIS BANK ADVANTAGE =================== -->
    <div class="slide" id="s12">
        <div class="bg-glow glow-2 pulse"></div>
        <p class="slide-tag">The Partnership Synergy</p>
        <h2 class="slide-title">The Axis Bank Commercial Advantage</h2>
        <p class="slide-subtitle">Capturing the mandate translates directly to massive CASA growth and steady fee income.</p>
        <div class="grid-3 stagger" style="margin-top:10px">
            <div class="card" style="border-top:3px solid var(--green)">
                <div class="card-icon" style="background:rgba(0,200,83,.15);color:var(--green)"><i class="fas fa-money-bill-trend-up"></i></div>
                <h3>Massive CASA Acquisition</h3>
                <p>Mandating Axis as the SNA bank brings &nbsp;Thousands of Crores in stable, low-cost deposits from State consolidated funds.</p>
            </div>
            <div class="card" style="border-top:3px solid var(--axis)">
                <div class="card-icon" style="background:var(--axis-glow);color:var(--axis-light)"><i class="fas fa-chart-line"></i></div>
                <h3>Aggregated Float Yield</h3>
                <p>Centralized holding in Node 1 accounts allows Axis to maximize yield on float before ultimate vendor settlement dates.</p>
            </div>
            <div class="card" style="border-top:3px solid var(--gold)">
                <div class="card-icon" style="background:rgba(255,215,0,.15);color:var(--gold)"><i class="fas fa-hand-holding-dollar"></i></div>
                <h3>Transaction Fee Annuity</h3>
                <p>Millions of micro and macro vendor payments generate consistent NEFT/RTGS transaction fee revenue across all 16FC cycles.</p>
            </div>
        </div>
    </div>
"""

    new_s14_to_s19 = """
    <!-- =================== SLIDE 14: CASE STUDIES =================== -->
    <div class="slide" id="s14">
        <div class="bg-glow glow-1 pulse"></div>
        <p class="slide-tag">Measured Impact</p>
        <h2 class="slide-title">Case Studies &amp; Metrics</h2>
        <div class="grid-2 stagger" style="margin-top:20px;max-width:1000px">
            <div class="card" style="border-left:4px solid var(--axis)">
                <h3 style="color:var(--axis-light);margin-bottom:8px">State Nodal Agency Deployment</h3>
                <p style="font-size:.8rem;color:var(--gray);margin-bottom:16px">Digitized completely offline block-level allocation for 400+ Urban Local Bodies (ULBs).</p>
                <div style="display:flex;gap:20px">
                    <div>
                        <div style="font-size:1.6rem;font-weight:800;font-family:var(--font-head);color:var(--green)">&#8377;1,200 Cr+</div>
                        <div style="font-size:.7rem;color:var(--gray)">Funds Tracked</div>
                    </div>
                    <div>
                        <div style="font-size:1.6rem;font-weight:800;font-family:var(--font-head);color:var(--blue)">100%</div>
                        <div style="font-size:.7rem;color:var(--gray)">UC Compliance Rate</div>
                    </div>
                </div>
            </div>
            <div class="card" style="border-left:4px solid var(--gold)">
                <h3 style="color:var(--gold);margin-bottom:8px">Panchayati Raj Institution (PRI)</h3>
                <p style="font-size:.8rem;color:var(--gray);margin-bottom:16px">Automated 15FC grant tranches across 12,000+ Gram Panchayats.</p>
                <div style="display:flex;gap:20px">
                    <div>
                        <div style="font-size:1.6rem;font-weight:800;font-family:var(--font-head);color:var(--green)">- 68 Days</div>
                        <div style="font-size:.7rem;color:var(--gray)">Avg. Disbursal Delay Reduced</div>
                    </div>
                    <div>
                        <div style="font-size:1.6rem;font-weight:800;font-family:var(--font-head);color:var(--blue)">0%</div>
                        <div style="font-size:.7rem;color:var(--gray)">Idle Float at GP Level</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- =================== SLIDE 15: SNA FUND FLOW =================== -->
    <div class="slide" id="s15">
        <div class="bg-glow glow-3 pulse"></div>
        <p class="slide-tag">Financial Architecture</p>
        <h2 class="slide-title">Just-In-Time (JIT) Implementation</h2>
        <div style="max-width:900px;margin-top:10px;text-align:center">
            <img src="https://placehold.co/900x450/111827/4f46e5?text=SNA+Fund+Flow+Architecture+Diagram" alt="SNA Validated Fund Flow" class="fund-flow-img" style="margin-bottom:16px;border-radius:12px;" />
            <div style="display:flex;justify-content:space-around;font-size:.8rem;color:var(--gray);text-align:left;background:var(--card-bg);padding:16px;border-radius:12px;border:1px solid var(--card-border)">
                <div><strong>1. RBI / GoI:</strong> Tranche released to State</div>
                <div><strong>2. State SNA:</strong> Axis Bank main holding account</div>
                <div><strong>3. PFMS Check:</strong> ZBSA drawing limit validated</div>
                <div><strong>4. Vendor RTGS:</strong> Instant direct settlement</div>
            </div>
        </div>
    </div>

    <!-- =================== SLIDE 16: SECURITY & RISK =================== -->
    <div class="slide" id="s16">
        <div class="bg-glow glow-2 pulse"></div>
        <p class="slide-tag">Compliance Framework</p>
        <h2 class="slide-title">Enterprise Security &amp; Risk Mitigation</h2>
        <div class="grid-3 stagger" style="margin-top:10px">
            <div class="card" style="border-top:3px solid var(--axis)">
                <div class="card-icon" style="background:var(--axis-glow);color:var(--axis-light)"><i class="fas fa-lock"></i></div>
                <h3>Military-Grade Encryption</h3>
                <p>AES-256 for data at rest. TLS 1.3 for all flight payloads between mobile, cloud, and Axis CBS APIs.</p>
            </div>
            <div class="card" style="border-top:3px solid var(--blue)">
                <div class="card-icon" style="background:var(--blue-glow);color:var(--blue)"><i class="fas fa-database"></i></div>
                <h3>Data Residency</h3>
                <p>100% MEITY-empanelled localized India cloud hosting ensuring strict adherence to Data Protection Acts.</p>
            </div>
            <div class="card" style="border-top:3px solid var(--green)">
                <div class="card-icon" style="background:rgba(0,200,83,.15);color:var(--green)"><i class="fas fa-file-signature"></i></div>
                <h3>Immutable Audit Logs</h3>
                <p>Blockchain-inspired append-only audit ledgers. Every login, photo captured, and approval clicked is eternally traceable.</p>
            </div>
        </div>
    </div>

    <!-- =================== SLIDE 17: ROLLOUT PLAN =================== -->
    <div class="slide" id="s17">
        <div class="bg-glow glow-1 pulse"></div>
        <p class="slide-tag">Execution Strategy</p>
        <h2 class="slide-title">The 90-Day Production Rollout</h2>
        <div style="max-width:1000px;margin-top:20px" class="stagger">
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:20px;background:var(--card-bg);padding:20px;border-radius:16px;border-left:4px solid var(--axis)">
                <div style="font-size:2rem;font-weight:800;color:var(--axis-light);min-width:80px;text-align:right">0&#8211;30&nbsp;</div>
                <div>
                    <h3 style="font-size:1.1rem;margin-bottom:6px;color:#fff">Phase 1: Integration &amp; UAT</h3>
                    <p style="font-size:.85rem;color:var(--gray)">Sandbox API handshake between Sketch Cloud and Axis Bank CBS. End-to-end security penetration testing and User Acceptance Testing with dummy nodal data.</p>
                </div>
            </div>
            <div style="display:flex;align-items:center;gap:20px;margin-bottom:20px;background:var(--card-bg);padding:20px;border-radius:16px;border-left:4px solid var(--blue)">
                <div style="font-size:2rem;font-weight:800;color:var(--blue);min-width:80px;text-align:right">30&#8211;60</div>
                <div>
                    <h3 style="font-size:1.1rem;margin-bottom:6px;color:#fff">Phase 2: District-Level Pilot</h3>
                    <p style="font-size:.85rem;color:var(--gray)">Live deployment in 1 target district. Onboarding 50 Junior Engineers. Processing real, low-value disbursements.</p>
                </div>
            </div>
            <div style="display:flex;align-items:center;gap:20px;background:var(--card-bg);padding:20px;border-radius:16px;border-left:4px solid var(--green)">
                <div style="font-size:2rem;font-weight:800;color:var(--green);min-width:80px;text-align:right">60&#8211;90</div>
                <div>
                    <h3 style="font-size:1.1rem;margin-bottom:6px;color:#fff">Phase 3: State-Wide Scale</h3>
                    <p style="font-size:.85rem;color:var(--gray)">Pan-state training rollout. Activation of ZBSA nodal accounts globally. Transition of all 16FC capital flow perfectly into the intelligence hub.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- =================== SLIDE 18: COMMERCIAL MODEL =================== -->
    <div class="slide" id="s18">
        <div class="bg-glow glow-2 pulse"></div>
        <p class="slide-tag">Partnership Framework</p>
        <h2 class="slide-title">Commercial &amp; Operational Model</h2>
        <div class="grid-2 stagger" style="margin-top:20px;max-width:950px">
            <div class="card" style="border-top:3px solid var(--blue)">
                <h3>Technology Partner (Sketch)</h3>
                <ul style="font-size:.8rem;color:var(--gray);line-height:1.8;padding-left:16px;margin-top:10px">
                    <li>Provides white-labeled Cloud Middleware, Mobile App, and Web Dashboard.</li>
                    <li>Handles server hosting, AI processing costs, and 24/7 technical support.</li>
                    <li>SaaS/Volume-based licensing fee charged directly to the State Department.</li>
                </ul>
            </div>
            <div class="card" style="border-top:3px solid var(--axis)">
                <h3>Banking Partner (Axis Bank)</h3>
                <ul style="font-size:.8rem;color:var(--gray);line-height:1.8;padding-left:16px;margin-top:10px">
                    <li>Provides the core SNA/ZBSA account architecture and PFMS API connectivity.</li>
                    <li>Retains 100% of the CASA deposits and idle float yield.</li>
                    <li>Retains 100% of the RTGS/NEFT transaction processing fees.</li>
                    <li>Zero upfront CAPEX for software R&D.</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- =================== SLIDE 19: THE ASK =================== -->
    <div class="slide" id="s19">
        <div class="bg-glow glow-1 pulse"></div>
        <p class="slide-tag">Next Steps</p>
        <h2 class="slide-title">The Immediate Ask</h2>
        <div class="card stagger" style="max-width:800px;margin:20px auto 0;text-align:center;padding:40px;border:2px solid var(--axis)">
            <i class="fas fa-handshake-angle" style="font-size:3rem;color:var(--axis-light);margin-bottom:20px;display:block"></i>
            <h3 style="font-size:1.4rem;color:#fff;margin-bottom:16px">Exclusive Nodal Action Plan</h3>
            <p style="font-size:.95rem;color:var(--gray);line-height:1.7;margin-bottom:24px">
                We are seeking an exclusive, formal joint-bidding partnership with Axis Bank's Government Business Group to target the upcoming 16th Finance Commission RFP in a primary tier-1 state. 
            </p>
            <div style="display:inline-block;background:var(--axis-glow);color:var(--axis-light);padding:12px 24px;border-radius:8px;font-weight:700;font-family:var(--font-head);letter-spacing:.5px">
                Goal: Joint Pilot Kickoff within 45 Days
            </div>
        </div>
    </div>
"""

    final_html = html_up_to_s7 + new_s8 + s16_html + s17_html + new_s11_12 + s18_html + new_s14_to_s19 + s19_html

    with open('index_new.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Success. Run mv index_new.html index.html afterwards.")

if __name__ == '__main__':
    main()
