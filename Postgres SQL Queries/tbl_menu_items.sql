DROP TABLE IF EXISTS tbl_menu_items CASCADE;

CREATE TABLE tbl_menu_items (
    item_id SERIAL PRIMARY KEY,
    parent_id INTEGER REFERENCES tbl_menu_items(item_id),
    item_name VARCHAR(100) NOT NULL,
    item_type VARCHAR(50) NOT NULL CHECK (item_type IN ('category', 'tool', 'link')),
    route_path VARCHAR(255),
    icon_name VARCHAR(100), -- For Material-UI or Bootstrap Icons
    is_active BOOLEAN DEFAULT true,
    is_trending BOOLEAN DEFAULT false,
    is_promoted BOOLEAN DEFAULT false,
    tool_domain VARCHAR(100),
    seo_title VARCHAR(70),
    seo_meta_description VARCHAR(160),
    geo_target JSONB,
    click_count BIGINT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Add an index on parent_id for faster querying of hierarchical data
CREATE INDEX idx_tbl_menu_items_parent_id ON tbl_menu_items (parent_id);
-- Add a comment on the table for clarity
COMMENT ON TABLE tbl_menu_items IS 'Stores hierarchical data for the dynamic sidebar menu, including categories and tools.';

-- Top Level Categories (parent_id is NULL)
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name, seo_title, seo_meta_description) VALUES
    (NULL, 'Image Tools', 'category', '/image-tools', 'PhotoLibrary', 'Free Online Image Tools', 'A collection of free tools to edit, convert, and manage your images.'), -- item_id will be 1
    (NULL, 'Text Tools', 'category', '/text-tools', 'TextFields', 'Online Text & Content Tools', 'Manipulate and analyze your text with these free online utilities.'), -- item_id will be 2
    (NULL, 'Web Tools', 'category', '/web-tools', 'Language', 'Developer & Webmaster Tools', 'Essential tools for web developers and SEO professionals.'), -- item_id will be 3
    (NULL, 'File Converters', 'category', '/file-converters', 'SwapHoriz', 'Free Online File Converters', 'Convert your files from one format to another for free.'); -- item_id will be 4

-- Tools and Sub-categories under 'Image Tools' (parent_id = 1)
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name, tool_domain, seo_title, seo_meta_description) VALUES
    (1, 'Image Converter', 'tool', '/image-tools/converter', 'CompareArrows', 'Image Conversion', 'Free Image Converter | PNG, JPG, WEBP', 'Convert images between JPG, PNG, GIF, WEBP, and more formats.'),
    (1, 'Image Resizer', 'tool', '/image-tools/resizer', 'AspectRatio', 'Image Editing', 'Resize Images Online for Free', 'Easily resize your images by pixel dimensions or percentage.'),
    (1, 'Image Compressor', 'tool', '/image-tools/compressor', 'Compress', 'Image Optimization', 'Compress JPG & PNG Images', 'Reduce the file size of your images without losing quality.'),
    (1, 'Color Picker', 'tool', '/image-tools/color-picker', 'Colorize', 'Color Utility', 'Online Color Picker from Image', 'Upload an image and get HEX, RGB, and HSL color codes.');

-- Tools and Sub-categories under 'Text Tools' (parent_id = 2)
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name, tool_domain, seo_title, seo_meta_description) VALUES
    (2, 'Word Counter', 'tool', '/text-tools/word-counter', 'Abc', 'Content Analysis', 'Live Word and Character Counter', 'Count words, characters, sentences, and paragraphs in your text.'),
    (2, 'Lorem Ipsum Generator', 'tool', '/text-tools/lorem-ipsum', 'FormatQuote', 'Content Generation', 'Custom Lorem Ipsum Generator', 'Generate placeholder text for your designs and mockups.'),
    (2, 'Case Converter', 'tool', '/text-tools/case-converter', 'TextFormat', 'Text Formatting', 'Online Case Converter Tool', 'Convert text to UPPERCASE, lowercase, Title Case, and more.');

-- Tools and Sub-categories under 'Web Tools' (parent_id = 3)
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name, tool_domain, seo_title, seo_meta_description, is_promoted) VALUES
    (3, 'HTML Minifier', 'tool', '/web-tools/html-minifier', 'Code', 'Web Optimization', 'HTML Minifier Online', 'Minify your HTML code to reduce page load times.', false),
    (3, 'CSS Unminifier', 'tool', '/web-tools/css-unminifier', 'Css', 'Web Development', 'CSS Beautifier / Unminifier', 'Format and beautify your compressed CSS code to make it readable.', false),
    (3, 'JSON Viewer', 'tool', '/web-tools/json-viewer', 'DataObject', 'Web Development', 'JSON Viewer and Formatter', 'View, format, and validate your JSON data online.', true),
    (3, 'URL Encoder/Decoder', 'tool', '/web-tools/url-encoder', 'Link', 'Web Utility', 'Free URL Encoder & Decoder', 'Encode or decode text for use in URLs.', false);

-- Tools and Sub-categories under 'File Converters' (parent_id = 4)
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name, tool_domain, seo_title, seo_meta_description, is_trending, geo_target) VALUES
    (4, 'JSON to XML', 'tool', '/file-converters/json-to-xml', 'SyncAlt', 'Data Conversion', 'Convert JSON to XML Online', 'Free tool to convert your JSON data structures to XML format.', true, '["US", "GB", "IN"]'),
    (4, 'XML to JSON', 'tool', '/file-converters/xml-to-json', 'SyncAlt', 'Data Conversion', 'Convert XML to JSON Online', 'Free tool to convert your XML data structures to JSON format.', true, '["US", "GB", "IN"]'),
    (4, 'CSV to JSON', 'tool', '/file-converters/csv-to-json', 'TableRows', 'Data Conversion', 'Convert CSV to JSON Online', 'Transform your CSV files into structured JSON data.', false, NULL);

-- Example of a second-level sub-category
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name) VALUES
    (1, 'Advanced Filters', 'category', '/image-tools/filters', 'FilterBAndW'); -- item_id will be 16

-- Example of a tool under the second-level sub-category (parent_id = 16)
INSERT INTO tbl_menu_items (parent_id, item_name, item_type, route_path, icon_name, tool_domain, seo_title, seo_meta_description) VALUES
    (16, 'Black & White Filter', 'tool', '/image-tools/filters/bw', 'MonochromePhotos', 'Image Editing', 'Apply B&W Filter to Photos', 'Convert your color photos to black and white instantly.');


-- End of script
SELECT 'PL/pgSQL script executed successfully. Table tbl_menu_items has been recreated and populated.' AS status;
