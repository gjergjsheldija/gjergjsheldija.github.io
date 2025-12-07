---
title: "Consulting Services"
description: "Fixed-price packages to de-risk your architecture and accelerate compliance."
lead_magnet_link: "/files/mdr-fhir-checklist.pdf"
booking_link: "https://calendly.com/your-link"
---

<div class="grid md:grid-cols-3 gap-8">
  {{ range .Site.Data.services }}
    <div class="relative border rounded-lg p-6 flex flex-col {{ if .highlight }}border-blue-500 ring-2 ring-blue-500{{ else }}border-gray-200{{ end }}">
      {{ if .highlight }}
        <span class="absolute top-0 right-0 bg-blue-500 text-white text-xs font-bold px-3 py-1 rounded-bl-lg rounded-tr-lg -mt-px -mr-px">Most Popular</span>
      {{ end }}
      <h3 class="text-xl font-bold text-gray-900">{{ .title }}</h3>
      <p class="text-3xl font-extrabold text-gray-900 my-4">{{ .price }}</p>
      <p class="text-gray-600 flex-grow">{{ .description }}</p>
      <ul class="my-6 space-y-2">
        {{ range .features }}
          <li class="flex items-center">
            <svg class="w-5 h-5 text-green-500 mr-2 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            <span class="text-gray-700">{{ . }}</span>
          </li>
        {{ end }}
      </ul>
      <a href="{{ .link }}" class="mt-auto w-full text-center font-bold py-3 px-6 rounded-lg transition duration-300
        {{ if .highlight }}bg-blue-600 hover:bg-blue-700 text-white{{ else }}bg-gray-100 hover:bg-gray-200 text-gray-800{{ end }}">
        {{ .cta }}
      </a>
    </div>
  {{ end }}
</div>
