const q = (row["Company"] || "").trim().toLowerCase();
const d = row["apollo_company"]?.data || {};
const accts = d.accounts || [];
const orgs = d.organizations || [];
const pool = accts.length > 0 ? accts : orgs;
const a = pool.find(x => {
  const name = (x?.name || "").trim().toLowerCase();
  return name === q || name.includes(q) || q.includes(name);
}) || pool[0] || null;
if (!a) return null;
return {
  company_name: a.name || null,
  company_domain: a.primary_domain || a.domain || a.website_url?.replace(/^https?:\/\/(www\.)?/, '').replace(/\/$/, '') || null,
  company_linkedin: a.linkedin_url || null,
  employee_count: a.estimated_num_employees || null
};
