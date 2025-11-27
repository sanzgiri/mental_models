import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

const contentDirectory = path.join(process.cwd(), 'content');

export interface MentalModel {
    slug: string;
    title: string;
    content: string;
    summary: string; // The HTML content
    category?: string; // We might need to parse this from the CSV later or add to frontmatter
}

export function getAllModelSlugs() {
    if (!fs.existsSync(contentDirectory)) {
        return [];
    }
    const fileNames = fs.readdirSync(contentDirectory);
    return fileNames.map((fileName) => {
        return {
            params: {
                slug: fileName.replace(/\.md$/, ''),
            },
        };
    });
}

export function getSortedModelsData(): MentalModel[] {
    if (!fs.existsSync(contentDirectory)) {
        return [];
    }
    const fileNames = fs.readdirSync(contentDirectory);
    const allModelsData = fileNames.map((fileName) => {
        const slug = fileName.replace(/\.md$/, '');
        const fullPath = path.join(contentDirectory, fileName);
        const fileContents = fs.readFileSync(fullPath, 'utf8');

        // Use gray-matter to parse the post metadata section
        const matterResult = matter(fileContents);

        // Fallback title from filename if not in frontmatter (our script doesn't add frontmatter yet, just # Title)
        // We should probably update the script to add frontmatter, or parse the first line.
        // For now, let's assume the first line is the title if not in frontmatter.
        let title = matterResult.data.title;
        if (!title) {
            const lines = matterResult.content.split('\n');
            if (lines[0].startsWith('# ')) {
                title = lines[0].substring(2);
            } else {
                title = slug.replace(/-/g, ' ');
            }
        }

        return {
            slug,
            title,
            content: matterResult.content,
            summary: '', // We'll process markdown only when needed or here if list is small
            ...matterResult.data,
        };
    });

    return allModelsData.sort((a, b) => {
        if (a.title < b.title) {
            return -1;
        } else {
            return 1;
        }
    });
}

export async function getModelData(slug: string): Promise<MentalModel> {
    const fullPath = path.join(contentDirectory, `${slug}.md`);
    const fileContents = fs.readFileSync(fullPath, 'utf8');

    const matterResult = matter(fileContents);

    const processedContent = await remark()
        .use(html)
        .process(matterResult.content);
    const contentHtml = processedContent.toString();

    let title = matterResult.data.title;
    if (!title) {
        const lines = matterResult.content.split('\n');
        if (lines[0].startsWith('# ')) {
            title = lines[0].substring(2);
        } else {
            title = slug.replace(/-/g, ' ');
        }
    }

    return {
        slug,
        content: matterResult.content,
        summary: contentHtml,
        title,
        ...matterResult.data,
    };
}
