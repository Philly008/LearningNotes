import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.FilenameFilter;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

public class getClassFile {
	String subject = "";
	String sourceDir = "";
	String objectDir = "";

	public void init() {
		// NIP_REPORT_3.0.0.0,NIP_QUERY,NIP_CUS_3.0,NIP_3.5.0.0,NIP_TONGBU_3.5.0.0,NIP_WeiMon
		subject = "NIP_local";
		//subject = "NIP_3.5_release";
		sourceDir = this.getSourceDir(subject);
		objectDir = "E:/export/javaclasses/" + this.getFormatDate() + "/NIP/";
		//objectDir = "E:/export/javaclasses/NIP_3.5_release/" + this.getFormatDate() + "/NIP_3.5_release/";
	}

	private String getSourceDir(String subject) {
		String fileContext = "";
		if ("NIP_REPORT_local".equals(subject)) {
			//fileContext = "E:/3.5_release/NIP_3.5.0.0_release/WebContent/";
			fileContext = "E:/newworkspace/windows/local/NIP_REPORT_local/WebContent/";
		} else if ("NIP_local".equals(subject)) {
			fileContext = "E:/newworkspace/windows/local/NIP_local/WebContent/";
		} else if ("NIP_TONGBU_local".equals(subject)) {
			fileContext = "E:/newworkspace/windows/local/NIP_TONGBU_local/WebContent/";
		} else { 
			fileContext = "e:/xxt3/trunk/web/";
		}
		return fileContext;
	}

	public static void main(String[] args) {
		new getClassFile().run();
	}

	private void run() {
		this.init();
		int suc_num = 0;
		int fail_num = 0;
		int suc_dir_num = 0;
		int fail_dir_num = 0;
		int not_file_num = 0;
		try {
			BufferedReader br = new BufferedReader(new FileReader("E:/上线文件.txt"));
			String r = br.readLine();
			String r_init = "";
			while (r != null) {
				r = r.trim();
				if (r.indexOf(".") < 0 && !r.endsWith("*")) {
					System.out.println(r + "不是完整的文件路径！");
					not_file_num++;
					r = br.readLine();
					continue;
				}
				if (r.startsWith("web/")) {
					r = r.substring(4);
				}
				r = r.replaceAll("\\\\", "/");
				r_init = r;
				boolean flag = true;

				if (r.endsWith("*.java")) { // java文件全目录
					r = r.replaceAll("src/", "/");
					r = r.replaceAll(".java", ".class");
					r = "WEB-INF/classes/" + r;
					List<String> list = FileViewer1.getListFiles(sourceDir + r.substring(0, r.lastIndexOf("/") + 1), "",
							true);
					for (Iterator<String> i = list.iterator(); i.hasNext();) {
						String temp = (String) i.next();
						if (temp.indexOf(".svn") > 0) {
							continue;
						}
						temp = temp.replaceAll("\\\\", "/");
						flag = !flag ? false : CopyFile(temp, objectDir + temp.replaceAll(sourceDir, ""));
					}
					if (flag) {
						suc_dir_num++;
					} else {
						fail_dir_num++;
					}
				} else if (r.endsWith("*")) { // 其他文件全目录
					List<String> list = FileViewer1.getListFiles(sourceDir + r.substring(0, r.lastIndexOf("/") + 1), "",
							true);
					for (Iterator<String> i = list.iterator(); i.hasNext();) {
						String temp = (String) i.next();
						if (temp.indexOf(".svn") > 0) {
							continue;
						}
						temp = temp.replaceAll("\\\\", "/");
						flag = !flag ? false : CopyFile(temp, objectDir + temp.replaceAll(sourceDir, ""));
					}
					if (flag) {
						suc_dir_num++;
					} else {
						fail_dir_num++;
					}
				} else if (r.endsWith(".java")) {
					r = r.replaceAll("src/", "/");
					r = r.replaceAll(".java", ".class");
					r = "WEB-INF/classes/" + r;
					String[] names = new java.io.File(sourceDir + r.substring(0, r.lastIndexOf("/") + 1))
							.list(new ScriptFilenameFilter(".class"));
					for (int i = 0; i < names.length; i++) {
						if (names[i].startsWith(r.substring(r.lastIndexOf("/") + 1, r.lastIndexOf(".")))) {
							flag = !flag ? false : CopyFile(sourceDir + r.substring(0, r.lastIndexOf("/") + 1)
									+ names[i], objectDir + r.substring(0, r.lastIndexOf("/") + 1) + names[i]);
						}
					}
					if (flag) {
						suc_num++;
					} else {
						System.out.println(sourceDir + r + " 源文件不存在或复制过程出现异常!");
						fail_num++;
					}
				} else if (r.endsWith(".htm")) {
					if (!r.startsWith("WEB-INF/") && !r.startsWith("velocity/")) {
						r = "velocity/" + r;
					}
					if (!r.startsWith("WEB-INF/")) {
						r = "WEB-INF/" + r;
					}
					flag = CopyFile(sourceDir + r, objectDir + r);
					if (flag) {
						suc_num++;
					} else {
						// System.out.println(sourceDir + r_init +
						// "，htm文件，重新用原始路径找寻");
						flag = CopyFile(sourceDir + r_init, objectDir + r_init);
						if (flag) {
							suc_num++;
						} else {
							System.out.println(sourceDir + r_init + " 源文件不存在或复制过程出现异常!");
							fail_num++;
						}
					}
				} else {
					flag = CopyFile(sourceDir + r, objectDir + r);
					if (flag) {
						suc_num++;
					} else {
						System.out.println(sourceDir + r + " 源文件不存在或复制过程出现异常!");
						fail_num++;
					}
				}
				r = br.readLine();
			}
			System.out.println("获取文件结束，共处理" + (suc_dir_num + fail_dir_num + suc_num + fail_num + not_file_num)
					+ "，其中复制成功目录" + suc_dir_num + "，复制失败目录" + fail_dir_num + "，复制成功文件" + suc_num + "，复制失败文件" + fail_num
					+ "，排除非完整文件路径" + not_file_num);
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("文件读取出错！！");
		}

	}

	public class ScriptFilenameFilter implements FilenameFilter {
		private String suffix;

		public ScriptFilenameFilter(String suffix) {
			this.suffix = suffix;
		}

		public boolean accept(File dir, String name) {
			if (name.endsWith(suffix)) {
				return true;
			}
			return false;
		}

	}

	public boolean CopyFile(String oldFilePath, String newFilePath) {
		File dirFile;
		boolean bFile;
		try {
			if (oldFilePath == null || oldFilePath.trim().length() == 0 || newFilePath == null
					|| newFilePath.trim().length() == 0) {
				System.out.println("路径为空");
				return false;

			}
			// 获得原文件，判断文件是否存在
			File sfile = new File(oldFilePath);
			if (sfile.exists() == false) {
				// System.out.println(oldFilePath + " 原文件不存在");
				return false;
			}
			// 判断第二个路径，是否存在 不存在就创建该文件夹
			dirFile = new File(newFilePath.substring(0, newFilePath.lastIndexOf("/")));
			bFile = dirFile.exists();
			if (bFile == false) {
				// System.out.println("文件目录不存在，现在创建目录");
				bFile = dirFile.mkdirs();
				if (bFile == true) {
					// System.out.println("创建成功");
				} else {
					System.out.println(newFilePath.substring(0, newFilePath.lastIndexOf("/")) + " 目录创建不成功");
					System.exit(0);
				}
			}
			// 往目录里面copy文件
			// System.out.println(oldFilePath + " 文件已经存在，现在往文件夹COPY文件");
			String filename = sfile.getName();
			File tfile = new File(dirFile, filename);
			RandomAccessFile rdtfile = new RandomAccessFile(tfile, "rw");
			RandomAccessFile rdsfile = new RandomAccessFile(sfile, "r");
			byte[] contents = new byte[(int) rdsfile.length()];
			rdsfile.read(contents);
			rdsfile.close();

			rdtfile.write(contents);
			rdtfile.close();
			// System.out.println(newFilePath + " 文件复制成功!");
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println(oldFilePath + "复制失败，抛出异常！");
			return false;
		}
		return true;
	}

	public String getFormatDate() {
		return new SimpleDateFormat("yyyyMMddHHmm").format(new Date());
	}

}

class FileViewer1 {
	public static List<String> fileList = new ArrayList<String>();

	/**
	 * 
	 * @param path
	 *            文件路径
	 * @param suffix
	 *            后缀名
	 * @param isdepth
	 *            是否遍历子目录
	 * @return
	 */
	public static List<String> getListFiles(String path, String suffix, boolean isdepth) {
		fileList = new ArrayList<String>();
		File file = new File(path);
		return listFile(file, suffix, isdepth);
	}

	public static List<String> listFile(File f, String suffix, boolean isdepth) {
		// 是目录，同时需要遍历子目录
		if (f.isDirectory() && isdepth == true) {
			File[] t = f.listFiles();
			for (int i = 0; i < t.length; i++) {
				listFile(t[i], suffix, isdepth);
			}
		} else {
			String filePath = f.getAbsolutePath();

			// System.out.println("suffix = "+suffix);
			if (suffix == "" || suffix == null) {
				// 后缀名为null则为所有文件
				// System.out.println("----------------");
				fileList.add(filePath);
			} else {
				int begIndex = filePath.lastIndexOf(".");// 最后一个.(即后缀名前面的.)的索引
				String tempsuffix = "";

				if (begIndex != -1) {// 防止是文件但却没有后缀名结束的文件
					tempsuffix = filePath.substring(begIndex + 1, filePath.length());
				}

				if (tempsuffix.equals(suffix)) {
					fileList.add(filePath);
				}
			}

		}

		return fileList;
	}

	/**
	 * 方法追加文件：使用FileWriter
	 * 
	 * @param fileName
	 * @param content
	 */
	public static void appendMethod(String fileName, String content) {
		try {
			// 打开一个写文件器，构造函数中的第二个参数true表示以追加形式写文件
			FileWriter writer = new FileWriter(fileName, true);
			writer.write(content + "\r\n");
			writer.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
