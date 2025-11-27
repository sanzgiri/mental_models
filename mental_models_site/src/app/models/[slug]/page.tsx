import { getModelData, getAllModelSlugs } from '@/lib/api';
import Navbar from '@/components/Navbar';
import Link from 'next/link';
import { ArrowLeft } from 'lucide-react';

export async function generateStaticParams() {
    const paths = getAllModelSlugs();
    return paths.map((path) => ({
        slug: path.params.slug,
    }));
}

export default async function ModelPage({ params }: { params: Promise<{ slug: string }> }) {
    const { slug } = await params;
    const modelData = await getModelData(slug);

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <main className="max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
                <div className="mb-8">
                    <Link href="/" className="inline-flex items-center text-sm text-gray-500 hover:text-gray-900">
                        <ArrowLeft className="mr-2 h-4 w-4" />
                        Back to Catalog
                    </Link>
                </div>

                <article className="bg-white shadow-lg sm:rounded-xl overflow-hidden border border-gray-100">
                    <div className="px-6 py-8 sm:px-10 border-b border-gray-100 bg-gradient-to-r from-indigo-50 to-white">
                        <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl mb-2">
                            {modelData.title}
                        </h1>
                        {modelData.category && (
                            <span className="inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800">
                                {modelData.category}
                            </span>
                        )}
                    </div>
                    <div className="px-6 py-8 sm:px-10 prose prose-lg prose-indigo max-w-none text-gray-700">
                        <div dangerouslySetInnerHTML={{ __html: modelData.summary }} />
                    </div>
                </article>
            </main>
        </div>
    );
}
