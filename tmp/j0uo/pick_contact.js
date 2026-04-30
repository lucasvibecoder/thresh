const dl = row["dropleads_contacts"]?.data?.leads || [];
const ap = row["apollo_contacts"]?.data?.people || [];

// Merge all candidates
const candidates = [];
for (const l of dl) {
  candidates.push({
    full_name: l.fullName || "",
    title: l.title || "",
    linkedin_url: l.linkedinUrl || "",
    source: "dropleads"
  });
}
for (const p of ap) {
  const ln = p.last_name_obfuscated || "";
  candidates.push({
    full_name: (p.first_name || "") + " " + ln,
    title: p.title || "",
    linkedin_url: p.linkedin_url || "",
    apollo_id: p.id || "",
    source: "apollo"
  });
}

if (candidates.length === 0) return null;
return candidates;
