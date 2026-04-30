const bc = row["best_contact"]?.extracted_json || row["best_contact"]?.output || {};
return {
  first_name: bc.first_name || "",
  last_name: bc.last_name || "",
  full_name: bc.full_name || "",
  title: bc.title || "",
  linkedin_url: bc.linkedin_url || "",
  why_fit: bc.why_this_person || ""
};
