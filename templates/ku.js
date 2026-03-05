document.addEventListener("DOMContentLoaded", function () {

  fetch("/api/jobs")
	.then(response => response.json())
	.then(data => {

	  const container = document.getElementById("ku-job-container");
	  container.innerHTML = "";

	  data.forEach(job => {

		const jobCard = document.createElement("div");
		jobCard.className = "ku-job-card";

		jobCard.innerHTML = `
		  <div class="ku-job-title">${job.title}</div>

		  <div class="ku-job-row">
			<span class="ku-job-label">Organization Name: </span>
			<span class="ku-job-value">${job.organization}</span>
		  </div>

		  <div class="ku-job-row">
			<span class="ku-job-label">No of Posts: </span>
			<span class="ku-job-value">${job.posts}</span>
		  </div>

		  <div class="ku-job-row">
			<span class="ku-job-label">Job Location: </span>
			<span class="ku-job-value">${job.location}</span>
		  </div>

		  <div class="ku-job-row">
			<span class="ku-job-label">Post Name: </span>
			<span class="ku-job-value">${job.post_name}</span>
		  </div>

		  <div class="ku-job-row">
			<span class="ku-job-label">Salary: </span>
			<span class="ku-job-value">${job.salary}</span>
		  </div>
		`;

		container.appendChild(jobCard);
	  });

	})
	.catch(error => {
	  console.error("Error fetching jobs:", error);
	});

});