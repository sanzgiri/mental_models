import Navbar from '@/components/Navbar';

export default function About() {
    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <main className="max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
                <div className="bg-white shadow sm:rounded-lg overflow-hidden">
                    <div className="px-4 py-5 sm:px-6 border-b border-gray-200">
                        <h1 className="text-3xl font-bold leading-tight text-gray-900">
                            About Mental Models
                        </h1>
                    </div>
                    <div className="px-4 py-5 sm:p-6 prose prose-indigo max-w-none text-gray-700">
                        <p>
                            Mental models are frameworks for thinking. They help us simplify complexity, understand reality, and make better decisions.
                        </p>
                        <p>
                            This project aims to curate the most useful mental models from various disciplines—physics, economics, psychology, and more—and provide clear, actionable summaries.
                        </p>
                        <h3>How to use this site</h3>
                        <p>
                            Browse the catalog to find models that interest you. Each entry includes a core concept explanation, real-world examples, and practical applications.
                        </p>
                        <p>
                            <em>Generated with the help of AI.</em>
                        </p>
                    </div>
                </div>
            </main>
        </div>
    );
}
